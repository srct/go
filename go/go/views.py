# Django Imports
from django.conf import settings
from django.http import HttpResponseServerError  # Http404
from django.utils import timezone
from django.core.exceptions import PermissionDenied  # ValidationError
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, redirect

# App Imports
from go.models import URL, RegisteredUser
from go.forms import URLForm, SignupForm

# Other Imports
from datetime import timedelta

##############################################################################
"""
Define useful helper methods here.
"""


def is_approved(user):
    """
    This function checks if a user account has a corresponding RegisteredUser,
    thus checking if the user is approved.
    """

    try:
        registered = RegisteredUser.objects.get(username=user.username)
        return registered.approved
    except RegisteredUser.DoesNotExist:
        return False


def is_registered(user):
    """
    This function checks if a user account has a corresponding RegisteredUser,
    thus checking if the user is registered.
    """

    try:
        registered = RegisteredUser.objects.get(username=user.username)
        return True
    except RegisteredUser.DoesNotExist:
        return False


##############################################################################
"""
Define user views here.
"""


def index(request):
    """
    This view handles the homepage that the user is presented with when
    they request '/'. If they're not logged in, they're redirected to
    login. If they're logged in but not registered, they're given the
    not_registered error page. If they are logged in AND registered, they
    get the URL registration form.
    """

    # If the user is not authenticated, show them a public landing page.
    if not request.user.is_authenticated():
        return render(request, 'public_landing.html')

    # If the user isn't registered, don't give them any leeway.
    if not is_approved(request.user):
        return render(request, 'not_registered.html')

    url_form = URLForm()  # unbound form

    if request.method == 'POST':
        url_form = URLForm(request.POST)  # bind dat form
        if url_form.is_valid():

            # We don't commit the url object yet because we need to add its
            # owner, and parse its date field.
            url = url_form.save(commit=False)
            url.owner = request.user

            # If the user entered a short url, it's already been validated,
            # so accept it. If they did not, however, then generate a
            # random one and use that instead.
            short = url_form.cleaned_data.get('short').strip()
            if len(short) > 0:
                url.short = short
            else:
                # If the user didn't enter a short url, generate a random
                # one. However, if a random one can't be generated, return
                # a 500 server error.
                random_short = URL.generate_valid_short()
                if random_short is None:
                    return HttpResponseServerError(
                        render(request, '500.html', {})
                    )
                else:
                    url.short = random_short

            # Grab the expiration field value. It's currently an unsable
            # string value, so we need to parse it into a datetime object
            # relative to right now.
            expires = url_form.cleaned_data.get('expires')

            if expires == URLForm.DAY:
                url.expires = timezone.now() + timedelta(days=1)
            elif expires == URLForm.WEEK:
                url.expires = timezone.now() + timedelta(weeks=1)
            elif expires == URLForm.MONTH:
                url.expires = timezone.now() + timedelta(weeks=3)
            else:
                pass  # leave the field NULL

            # Make sure that our new URL object is clean, then save it and
            # let's redirect to view this baby.
            url.full_clean()
            url.save()
            return redirect('view', url.short)

    return render(request, 'core/index.html', {
        'form': url_form,
    },
    )


def view(request, short):
    """
    This view allows the user to view details about a URL. Note that they
    do not need to be logged in to view info.
    """

    domain = "%s://%s" % (request.scheme, request.META.get('HTTP_HOST')) + "/"

    url = get_object_or_404(URL, short__iexact=short)

    return render(request, 'view.html', {
        'url': url,
        'domain': domain,
    },
    )


@login_required
def my_links(request):
    """
    This view displays all the information about all of your URLs. You
    obviously need to be logged in to view your URLs.
    """

    if not is_approved(request.user):
        return render(request, 'not_registered.html')

    urls = URL.objects.filter(owner=request.user)

    domain = "%s://%s" % (request.scheme, request.META.get('HTTP_HOST')) + "/"

    return render(request, 'my_links.html', {
        'urls': urls,
        'domain': domain,
    },
    )


@login_required
def delete(request, short):
    """
    This view deletes a URL if you have the permission to. User must be
    logged in and registered, and must also be the owner of the URL.
    """

    if not is_approved(request.user):
        return render(request, 'not_registered.html')

    url = get_object_or_404(URL, short__iexact=short)
    if url.owner == request.user:
        url.delete()
        return redirect('my_links')
    else:
        raise PermissionDenied()


@login_required
def signup(request):
    """
    This view presents the user with a registration form. You can register
    yourself, or another person.

    """
    # Do not display signup page to registered or approved users (Staff can still see these pages)
    if is_registered(request.user) and not request.user.is_staff:
        return render(request, 'core/signup.html', {
            'registered': True,
            'approved': False,
        },
        )
    elif is_approved(request.user) and not request.user.is_staff:
        return render(request, 'core/signup.html', {
            'registered': True,
            'approved': True,
        },
        )

    signup_form = SignupForm(request, initial={'username': request.user.username})

    # Non-staff have the username field read-only and pre-filled
    if request.user.is_staff:
        signup_form = SignupForm(request)
    else:
        signup_form = SignupForm(request,
            initial={'username': request.user.username, 'full_name': request.user.first_name + " " + request.user.last_name})
        signup_form.fields['username'].widget.attrs['readonly'] = 'readonly'

    if request.method == 'POST':
        signup_form = SignupForm(request, request.POST,
            initial={'approved': False, 'username': request.user.username})
        signup_form.fields['username'].widget.attrs['readonly'] = 'readonly'

        if signup_form.is_valid():
            if not request.user.is_staff:
                username = request.user.username
            else:
                username = signup_form.cleaned_data.get('username')
            full_name = signup_form.cleaned_data.get('full_name')
            description = signup_form.cleaned_data.get('description')
            organization = signup_form.cleaned_data.get('organization')

            # Only send mail if we've defined the mailserver
            if settings.EMAIL_HOST and settings.EMAIL_PORT:
                user_mail = username + settings.EMAIL_DOMAIN
                # Email sent to notify Admins
                to_admin = EmailMessage(
                    'Signup from %s' % (request.user.username),
                    ######################
                    '%s signed up at %s\n\n'
                    'Username: %s\n'
                    'Organization: %s\n\n'
                    'Message: %s\n\n'
                    'You can contact the user directly by replying to this email or '
                    'reply all to contact the user and notfiy the mailing list.\n'
                    'Please head to go.gmu.edu/useradmin to approve or '
                    'deny this application.'
                    % (str(full_name), str(timezone.now()).strip(),
                    str(request.user.username), str(organization), str(description)),
                    ######################
                    settings.EMAIL_FROM,
                    [settings.EMAIL_TO],
                    reply_to=[user_mail]
                ).send(fail_silently=False)
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
            signup_form.save()
            return redirect('registered')

    return render(request, 'core/signup.html', {
        'form': signup_form,
        'registered': False,
    },
    )


def redirection(request, short):
    """
    This view redirects a user based on the short URL they requested.
    """

    url = get_object_or_404(URL, short__iexact=short)
    url.clicks = url.clicks + 1

    if 'qr' in request.GET:
        url.qrclicks += 1

    if 'social' in request.GET:
        url.socialclicks += 1

    url.save()

    """
    Include server-side tracking because there is no template displayed to
    the user which would include javascript tracking.
    """

    from piwikapi.tracking import PiwikTracker
    from django.conf import settings
    # First, if PIWIK variables are undefined, don't try to push
    if settings.PIWIK_SITE_ID != "" and settings.PIWIK_URL != "":
        try:
            piwiktracker = PiwikTracker(settings.PIWIK_SITE_ID, request)
            piwiktracker.set_api_url(settings.PIWIK_URL)
            piwiktracker.do_track_page_view('Redirect to %s' % url.target)
        # Second, if we do get an error, don't let that keep us from redirecting
        except:
            pass

    return redirect(url.target)


def staff_member_required(view_func, redirect_field_name=REDIRECT_FIELD_NAME, login_url='about'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, displaying the login page if necessary.
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
    if request.POST:
        userlist = request.POST.getlist('username')
        if '_approve' in request.POST:
            for name in userlist:
                toapprove = RegisteredUser.objects.get(username=name)
                toapprove.approved = True
                toapprove.save()
                if settings.EMAIL_HOST and settings.EMAIL_PORT:
                    user_mail = toapprove.username + settings.EMAIL_DOMAIN
                    send_mail(
                        'Your Account has been Approved!',
                        ######################
                        'Hey there %s,\n\n'
                        'The Go admins have reviewed your application and have '
                        'approved you to use Go!\n\n'
                        'Head over to go.gmu.edu to create your first address.\n\n'
                        '- Go Admins'
                        % (str(toapprove.full_name)),
                        ######################
                        settings.EMAIL_FROM,
                        [user_mail]
                    )
        elif '_deny' in request.POST:
            for name in userlist:
                todeny = RegisteredUser.objects.get(username=name)
                if settings.EMAIL_HOST and settings.EMAIL_PORT:
                    user_mail = todeny.username + settings.EMAIL_DOMAIN
                    send_mail(
                        'Your Account has been Denied!',
                        ######################
                        'Hey there %s,\n\n'
                        'The Go admins have reviewed your application and have '
                        'decided to not approve you to use Go.\n\n'
                        'Please reach out to srct@gmu.edu to appeal '
                        'this decision.\n\n'
                        '- Go Admins'
                        % (str(todeny.full_name)),
                        ######################
                        settings.EMAIL_FROM,
                        [user_mail]
                    )
                todeny.delete()
    need_approval = RegisteredUser.objects.filter(approved=False)
    return render(request, 'admin/useradmin.html', {
        'need_approval': need_approval
    },
    )
