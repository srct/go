"""
go/views.py
"""

# Python stdlib imports
from datetime import timedelta

# Django Imports
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied  # ValidationError
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponseServerError  # Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

# Other imports
from ratelimit.decorators import ratelimit

# App Imports
from .forms import URLForm, EditForm
from .models import URL, RegisteredUser

def index(request):
    """
    If a user is logged in, this view displays all the information about all
    of their URLs. Otherwise, it will show the public landing page
    """

    # If the user is not authenticated, show them a public landing page.
    if not request.user.is_authenticated:
        return render(request, 'public_landing.html')

    # Get the current domain info
    domain = "%s://%s" % (request.scheme, request.META.get('HTTP_HOST')) + "/"

    # Grab a list of all the URL's that are currently owned by the user
    urls = URL.objects.filter(owner=request.user.registereduser)

    # Render my_links passing the list of URL's and Domain to the template
    return render(request, 'index.html', {
        'urls': urls,
        'domain': domain,
    })

@login_required
def new_link(request):
    """
    This view handles the homepage that the user is presented with when
    they request '/newLink'. If they're not logged in, they're redirected to
    login.
    """

    # If the user is blocked, then display the you're blocked page.
    if request.user.registereduser.blocked:
        return render(request, 'banned.html')

    # Initialize a URL form
    url_form = URLForm(host=request.META.get('HTTP_HOST'))  # unbound form

    # If a POST request is received, then the user has submitted a form and it's
    # time to parse the form and create a new URL object
    if request.method == 'POST':
        # Now we initialize the form again but this time we have the POST
        # request
        return _new_link_post(request)

    # Render index.html passing the form to the template
    return render(request, 'link.html', {
        'form': url_form,
    })

def _new_link_post(request):
    """
    This view handles when a POST is received from the link form.
    """
    url_form = URLForm(request.POST, host=request.META.get('HTTP_HOST'))

    if not url_form.is_valid():
        # there is an error, redisplay the form with the validation errors
        # Render index.html passing the form to the template
        return render(request, 'link.html', {
            'form': url_form,
        })

    # Call our post method to assemble our new URL object
    res = post(request, url_form)

    # If there is a 500 error returned, handle it
    if res == 500:
        return HttpResponseServerError(render(request, '500.html'))

    # Redirect to the shiny new URL
    return redirect('view', res.short)

@login_required
def my_links(request):
    """
    for compatibility, just in case
    shows the same thing as /, but requires login to be consistent with
    /newLink
    """
    if request.user.registereduser.blocked:
        return render(request, 'banned.html')
    return index(request)

# Rate limits are completely arbitrary
@ratelimit(key='user', rate='3/m', method='POST', block=True)
@ratelimit(key='user', rate='25/d', method='POST', block=True)
def post(request, url_form):
    """
    Helper function that handles POST requests for the URL creation
    """

    # We don't commit the url object yet because we need to add its
    # owner, and parse its date field.
    url = url_form.save(commit=False)
    url.owner = request.user.registereduser

    # If the user entered a short url, it's already been validated,
    # so accept it. If they did not, however, then generate a
    # random one and use that instead.
    short = url_form.cleaned_data.get('short').strip()

    # Check if a short URL was entered
    if len(short) > 0:
        url.short = short
    else:
        # If the user didn't enter a short url, generate a random
        # one. However, if a random one can't be generated, return
        # a 500 server error.
        random_short = URL.generate_valid_short()

        if random_short is None:
            return 500

        url.short = random_short

    # Grab the expiration field value. It's currently an unsable
    # string value, so we need to parse it into a datetime object
    # relative to right now.
    expires = url_form.cleaned_data.get('expires')

    # Determine what the expiration date is
    if expires == URLForm.DAY:
        url.expires = timezone.now() + timedelta(days=1)
    elif expires == URLForm.WEEK:
        url.expires = timezone.now() + timedelta(weeks=1)
    elif expires == URLForm.MONTH:
        url.expires = timezone.now() + timedelta(weeks=3)
    # elif expires == URLForm.CUSTOM:
    #     url.expires = url_form.cleaned_data.get('expires_custom')
    else:
        pass  # leave the field NULL

    # Make sure that our new URL object is clean, then save it and
    # let's redirect to view this baby.
    url.full_clean()
    url.save()
    return url

def view(request, short):
    """
    This view allows the user to "view details" about a URL. Note that they
    do not need to be logged in to view this information.
    """

    # Get the current domain info
    domain = "%ss://%s" % (request.scheme, request.META.get('HTTP_HOST')) + "/"

    # Get the URL that is being requested
    url = get_object_or_404(URL, short__iexact=short)

    # Render view.html passing the specified URL and Domain to the template
    return render(request, 'view.html', {
        'url': url,
        'domain': domain,
    })

@login_required
def edit(request, short):
    """
    This view allows a logged in user to edit the details of a Go link that they
    own. They can modify any value that they wish. If `short` is modified then
    we will need to create a new link and copy over stats from the previous.
    """

    # Do not allow unapproved users to edit links
    if request.user.registereduser.blocked:
        return render(request, 'banned.html')

    # Get the URL that is going to be edited
    url = get_object_or_404(URL, short__iexact=short)

    # If the RegisteredUser is the owner of the URL
    if url.owner == request.user.registereduser:

        # If a POST request is received, then the user has submitted a form and it's
        # time to parse the form and edit that URL object
        if request.method == 'POST':
            # Now we initialize the form again but this time we have the POST
            # request
            url_form = EditForm(request.POST, host=request.META.get('HTTP_HOST'))

            # Make a copy of the old URL
            copy = url
            # Remove the old one
            url.delete()

            # Django will check the form to make sure it's valid
            if url_form.is_valid():
                # If the short changed then we need to create a new object and
                # migrate some data over
                if url_form.cleaned_data.get('short').strip() != copy.short:
                    # Parse the form and create a new URL object
                    res = post(request, url_form)

                    # If there is a 500 error returned, handle it
                    if res == 500:
                        return HttpResponseServerError(render(request, '500.html'))

                    # We can procede with the editing process
                    else:
                        # Migrate clicks data
                        res.clicks = copy.clicks
                        res.qrclicks = copy.qrclicks
                        res.socialclicks = copy.socialclicks

                        # Save the new URL
                        res.save()

                        # Redirect to the shiny new *edited URL
                        return redirect('view', res.short)

                # The short was not edited and thus, we can directly edit the url
                else:
                    if url_form.cleaned_data.get('target').strip() != copy.target:
                        copy.target = url_form.cleaned_data.get('target').strip()
                        copy.save()

                    # Grab the expiration field value. It's currently an unsable
                    # string value, so we need to parse it into a datetime object
                    # relative to right now.
                    expires = url_form.cleaned_data.get('expires')

                    # Determine what the expiration date is
                    if expires == URLForm.DAY:
                        edited_expires = timezone.now() + timedelta(days=1)
                    elif expires == URLForm.WEEK:
                        edited_expires = timezone.now() + timedelta(weeks=1)
                    elif expires == URLForm.MONTH:
                        edited_expires = timezone.now() + timedelta(weeks=3)
                    elif expires == URLForm.CUSTOM:
                        edited_expires = url_form.cleaned_data.get('expires_custom')
                    else:
                        pass  # leave the field NULL

                    if edited_expires != copy.expires:
                        copy.expires = edited_expires
                        copy.save()

                    # Redirect to the shiny new *edited URL
                    return redirect('view', copy.short)

            # Else, there is an error, redisplay the form with the validation errors
            else:
                # Render index.html passing the form to the template
                return render(request, 'link.html', {
                    'form': url_form
                })
        else:
            # Initial data set here
            if url.expires != None:
                # Initialize a URL form with an expire date
                url_form = EditForm(host=request.META.get('HTTP_HOST'), initial={
                    'target': url.target,
                    'short': url.short,
                    'expires': 'Custom Date',
                    'expires_custom': url.expires
                })  # unbound form
            else:
                # Initialize a URL form without an expire date
                url_form = EditForm(host=request.META.get('HTTP_HOST'), initial={
                    'target': url.target,
                    'short': url.short,
                    'expires': 'Never',
                })  # unbound form

            # Render index.html passing the form to the template
            return render(request, 'link.html', {
                'form': url_form
            })
    else:
        # do not allow them to edit
        raise PermissionDenied()

@login_required
def delete(request, short):
    """
    This view deletes a URL if you have the permission to. User must be
    logged in and registered, and must also be the owner of the URL.
    """

    # Get the URL that is going to be deleted
    url = get_object_or_404(URL, short__iexact=short)

    if url.owner != request.user.registereduser:
        # do not allow them to delete
        raise PermissionDenied()

    url.delete()
    return redirect('my_links')

def redirection(request, short):
    """
    This view redirects a user based on the short URL they requested.
    """

    # Get the current domain info
    domain = "%s://%s" % (request.scheme, request.META.get('HTTP_HOST')) + "/"

    # Get the URL object that relates to the requested Go link
    url = get_object_or_404(URL, short__iexact=short)
    # Increment our clicks by one
    url.clicks += 1
    # Get the URL short link
    doesExist = URL.objects.get(short__iexact=short)
    # Checks to see if the link exists, if not we 404 the user.
    if doesExist.target is None:
        return redirect('go/404.html')
    # If the user is trying to make a Go link to itself, we 404 them
    if url.target == domain + short:
        return redirect('404.html')

    # If the user is coming from a QR request then increment qrclicks
    if 'qr' in request.GET:
        url.qrclicks += 1

    # If the user is coming from a social media request then increment qrclicks
    if 'social' in request.GET:
        url.socialclicks += 1

    # Save our data and redirect the user towards thier destination
    url.save()
    return redirect(url.target)

def staff_member_required(view_func, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    """
    Decorator function for views that checks that the user is logged in and is
    a staff member, displaying the login page if necessary.
    """

    return user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )(view_func)

@staff_member_required
def useradmin(request):
    """
    This view is a simplified admin panel, so that staff don't need to log in
    to approve links
    """

    # If we receive a POST request
    if request.POST:
        return _useradmin_post(request)

    # Get a list of all RegisteredUsers that need to be approved
    current_users = RegisteredUser.objects.filter(blocked=False)
    # Get a list of all RegisteredUsers that are blocked
    blocked_users = RegisteredUser.objects.filter(blocked=True)

    # Pass that list to the template
    return render(request, 'useradmin.html', {
        'current_users': current_users,
        'blocked_users': blocked_users
    })

def _useradmin_post(request):
    # Get a list of the potential victims (users)
    userlist = request.POST.getlist('username')

    # If we're blocking users
    if '_block' in request.POST:
        for name in userlist:
            to_block = RegisteredUser.objects.get(user__username__exact=name)
            if settings.EMAIL_HOST and settings.EMAIL_PORT:
                user_mail = to_block.user.username + settings.EMAIL_DOMAIN
                send_mail(
                    'Your Account has been Blocked!',
                    ######################
                    'Hey there %s,\n\n'
                    'The Go admins have reviewed your application and have '
                    'blocked you from using Go.\n\n'
                    'Please reach out to srct@gmu.edu to appeal '
                    'this decision.\n\n'
                    '- Go Admins'
                    % (str(to_block.full_name)),
                    ######################
                    settings.EMAIL_FROM,
                    [user_mail]
                )
            to_block.blocked = True
            to_block.save()

    # If we're un-blocking users
    elif '_unblock' in request.POST:
        for name in userlist:
            to_un_block = RegisteredUser.objects.get(user__username__exact=name)
            if settings.EMAIL_HOST and settings.EMAIL_PORT:
                user_mail = to_un_block.user.username + settings.EMAIL_DOMAIN
                send_mail(
                    'Your Account has been Un-Blocked!',
                    ######################
                    'Hey there %s,\n\n'
                    'The Go admins have reviewed your application and have '
                    'Un-Blocked you from using Go.\n\n'
                    'Congratulations! '
                    '- Go Admins'
                    % (str(to_un_block.full_name)),
                    ######################
                    settings.EMAIL_FROM,
                    [user_mail]
                )
            to_un_block.blocked = False
            to_un_block.save()
            return HttpResponseRedirect('useradmin')
