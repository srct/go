"""
go/views.py
"""

# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

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
from .forms import SignupForm, URLForm, EditForm
from .models import URL, RegisteredUser


def index(request):
    """
    If a user is logged in, this view displays all the information about all
    of their URLs. Otherwise, it will show the public landing page
    """

    # If the user is not authenticated, show them a public landing page.
    if not request.user.is_authenticated():
        return render(request, 'public_landing.html')

    # Get the current domain info
    domain = "%ss://%s" % (request.scheme, request.META.get('HTTP_HOST')) + "/"

    # Grab a list of all the URL's that are currently owned by the user
    urls = URL.objects.filter(owner=request.user.registereduser)

    # Render my_links passing the list of URL's and Domain to the template
    return render(request, 'core/index.html', {
        'urls': urls,
        'domain': domain,
    })

@login_required
def new_link(request):
    """
    This view handles the homepage that the user is presented with when
    they request '/newLink'. If they're not logged in, they're redirected to
    login. If they're logged in but not registered, they're given the
    not_registered error page. If they are logged in AND registered, they
    get the URL registration form.
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
        url_form = URLForm(request.POST, host=request.META.get('HTTP_HOST'))

        # Django will check the form to make sure it's valid
        if url_form.is_valid():
            # Call our post method to assemble our new URL object
            res = post(request, url_form)

            # If there is a 500 error returned, handle it
            if res == 500:
                return HttpResponseServerError(render(request, '500.html'))

            # Redirect to the shiny new URL
            return redirect('view', res.short)

        # Else, there is an error, redisplay the form with the validation errors
        else:
            # Render index.html passing the form to the template
            return render(request, 'core/new_link.html', {
                'form': url_form,
            })


    # Render index.html passing the form to the template
    return render(request, 'core/new_link.html', {
        'form': url_form,
    })

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
        else:
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
    elif expires == URLForm.CUSTOM:
        url.expires = url_form.cleaned_data.get('expires_custom')
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
                return render(request, 'core/edit_link.html', {
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
            return render(request, 'core/edit_link.html', {
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

    # If the RegisteredUser is the owner of the URL
    if url.owner == request.user.registereduser:
        # remove the URL
        url.delete()
        # redirect to my_links
        return redirect('my_links')
    else:
        # do not allow them to delete
        raise PermissionDenied()

@login_required
def signup(request):
    """
    This view presents the user with a registration form. You can register
    yourself.
    """

    # Do not display signup page to registered or approved users
    if request.user.registereduser.blocked:
        return render(request, 'banned.html')
    elif request.user.registereduser.approved:
        return redirect('/')
    elif request.user.registereduser.registered:
        return redirect('registered')

    # Initialize our signup form
    signup_form = SignupForm(
        request,
        initial={
            'full_name': request.user.first_name + " " + request.user.last_name
        }
    )

    # Set the full_name field to readonly since CAS will fill that in for them
    signup_form.fields['full_name'].widget.attrs['readonly'] = 'readonly'

    # If a POST request is received, then the user has submitted a form and it's
    # time to parse the form and create a new RegisteredUser
    if request.method == 'POST':
        # Now we initialize the form again but this time we have the POST
        # request
        signup_form = SignupForm(
            request, request.POST, instance=request.user.registereduser,
            initial={
                'full_name': request.user.first_name + " " + request.user.last_name
            }
        )

        # set the readonly flag again for good measure
        signup_form.fields['full_name'].widget.attrs['readonly'] = 'readonly'

        # Django will check the form to make sure it's valid
        if signup_form.is_valid():
            # Grab data from the form and store into variables
            description = signup_form.cleaned_data.get('description')
            full_name = signup_form.cleaned_data.get('full_name')
            organization = signup_form.cleaned_data.get('organization')

            # Only send mail if we've defined the mailserver
            if settings.EMAIL_HOST and settings.EMAIL_PORT:
                user_mail = request.user.username + settings.EMAIL_DOMAIN
                # Email sent to notify Admins
                to_admin = EmailMessage(
                    'Signup from %s' % (request.user.registereduser.user),
                    ######################
                    '%s signed up at %s\n\n'
                    'Username: %s\n'
                    'Organization: %s\n\n'
                    'Message: %s\n\n'
                    'You can contact the user directly by replying to this email or '
                    'reply all to contact the user and notfiy the mailing list.\n'
                    'Please head to go.gmu.edu/useradmin to approve or '
                    'deny this application.'
                    %(
                        str(full_name), str(timezone.now()).strip(),
                        str(request.user.registereduser.user), str(organization),
                        str(description)
                    ),
                    ######################
                    settings.EMAIL_FROM,
                    [settings.EMAIL_TO],
                    reply_to=[user_mail]
                )
                to_admin.send()
                # Confirmation email sent to Users
                send_mail(
                    'We have received your Go application!',
                    ######################
                    'Hey there %s,\n\n'
                    'The Go admins have received your application and are '
                    'currently in the process of reviewing it.\n\n'
                    'You will receive another email when you have been '
                    'approved.\n\n'
                    '- Go Admins'
                    % (str(full_name)),
                    ######################
                    settings.EMAIL_FROM,
                    [user_mail]
                )

            # Make sure that our new RegisteredUser object is clean, then save
            # it and let's redirect to tell the user they have registered.
            signup_form.save()
            return redirect('registered')

    # render signup.html passing along the form and the current registered
    # status
    return render(request, 'core/signup.html', {
        'form': signup_form,
        'registered': False,
    })

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
        # Get a list of the potential victims (users)
        userlist = request.POST.getlist('username')
        # If we're approving users
        if '_approve' in request.POST:
            for name in userlist:
                to_approve = RegisteredUser.objects.get(user__username__exact=name)
                to_approve.approved = True
                to_approve.save()

                # Send an email letting them know they are approved
                if settings.EMAIL_HOST and settings.EMAIL_PORT:
                    user_mail = to_approve.user.username + settings.EMAIL_DOMAIN
                    send_mail(
                        'Your Account has been Approved!',
                        ######################
                        'Hey there %s,\n\n'
                        'The Go admins have reviewed your application and have '
                        'approved you to use Go!\n\n'
                        'Head over to go.gmu.edu to create your first address.\n\n'
                        '- Go Admins'
                        % (str(to_approve.full_name)),
                        ######################
                        settings.EMAIL_FROM,
                        [user_mail]
                    )

        # If we're denying users
        elif '_deny' in request.POST:
            for name in userlist:
                to_deny = RegisteredUser.objects.get(user__username__exact=name)
                if settings.EMAIL_HOST and settings.EMAIL_PORT:
                    user_mail = to_deny.user.username + settings.EMAIL_DOMAIN
                    # Send an email letting them know they are denied
                    send_mail(
                        'Your Account has been Denied!',
                        ######################
                        'Hey there %s,\n\n'
                        'The Go admins have reviewed your application and have '
                        'decided to not approve you to use Go.\n\n'
                        'Please reach out to srct@gmu.edu to appeal '
                        'this decision.\n\n'
                        '- Go Admins'
                        % (str(to_deny.full_name)),
                        ######################
                        settings.EMAIL_FROM,
                        [user_mail]
                    )
                # Delete their associated RegisteredUsers
                to_deny.user.delete()
                return HttpResponseRedirect('useradmin')

        # If we're blocking users
        elif '_block' in request.POST:
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
                to_block.approved = False
                to_block.registered = False
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
                        'If you wish to continue Go use please register again. \n\n'
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

        # If we're removing existing users
        elif '_remove' in request.POST:
            for name in userlist:
                to_remove = RegisteredUser.objects.get(user__username__exact=name)
                if settings.EMAIL_HOST and settings.EMAIL_PORT:
                    user_mail = to_remove.user.username + settings.EMAIL_DOMAIN
                    send_mail(
                        'Your Account has been Deleted!',
                        ######################
                        'Hey there %s,\n\n'
                        'The Go admins have decided to remove you from Go. \n\n'
                        'Please reach out to srct@gmu.edu to appeal '
                        'this decision.\n\n'
                        '- Go Admins'
                        % (str(to_remove.full_name)),
                        ######################
                        settings.EMAIL_FROM,
                        [user_mail]
                    )
                to_remove.user.delete()
                return HttpResponseRedirect('useradmin')

    # Get a list of all RegisteredUsers that need to be approved
    need_approval = RegisteredUser.objects.filter(registered=True).filter(
        approved=False).filter(blocked=False)
    # Get a list of all RegisteredUsers that are currently users
    current_users = RegisteredUser.objects.filter(approved=True).filter(
        registered=True).filter(blocked=False)
    # Get a list of all RegisteredUsers that are blocked
    blocked_users = RegisteredUser.objects.filter(blocked=True)

    # Pass that list to the template
    return render(request, 'admin/useradmin.html', {
        'need_approval': need_approval,
        'current_users': current_users,
        'blocked_users': blocked_users
    })
