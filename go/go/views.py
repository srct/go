from go.models import URL, RegisteredUser
from go.forms import URLForm, SignupForm
from datetime import timedelta
from django.conf import settings
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import os

def is_registered( user ):
    try:
        registered = RegisteredUser.objects.get( username=user.username )
        return True
    except RegisteredUser.DoesNotExist:
        return False

# Error 404
def error_404(request):
    return render(request, '404.html', {
    },
    )

# Error 500
def error_500(request):
    return render(request, '500.html', {
    },
    )

# Homepage view.
@login_required
def index(request):

    if not is_registered(request.user):
        return render(request, 'not_registered.html')

    url_form = URLForm() # unbound form
    errors = []

    if request.method == 'POST':
        url_form = URLForm( request.POST ) # bind dat form
        if url_form.is_valid():

            url = url_form.save(commit=False)
            url.owner = request.user

            short = url_form.cleaned_data.get('short').strip()
            if len(short) > 0:
                url.short = short
            else:
                url.short = URL.generate_valid_short()

            expires = url_form.cleaned_data.get('expires')

            if expires == URLForm.DAY:
                url.expires = timezone.now() + timedelta(days=1)
            elif expires == URLForm.WEEK:
                url.expires = timezone.now() + timedelta(weeks=1)
            elif expires == URLForm.MONTH:
                url.expires = timezone.now() + timedelta(weeks=3)
            else:
                pass # leave the field NULL

            url.full_clean()
            url.save()
            return redirect('view', url.short)

    return render(request, 'index.html', {
        'form': url_form,
    },
    )

# Preview a link.
def view(request, short):
    url = get_object_or_404(URL, short__iexact = short)
    return render(request, 'view.html', {
        'url': url,
    },
    )

# My-Links page.
@login_required
def my_links(request):
    if not is_registered(request.user):
        return render(request, 'not_registered.html')
    urls = URL.objects.filter( owner = request.user )
    return render(request, 'my_links.html', {
        'urls' : urls,
    },
    )

# Delete link page.
@login_required
def delete(request, short):
    if not is_registered(request.user):
        return render(request, 'not_registered.html')
    url = get_object_or_404(URL, short__iexact = short )
    if url.owner == request.user:
        url.delete()
        return redirect('my_links')
    else:
        raise PermissionDenied()

# About page, static.
def about(request):
    return render(request, 'about.html', {

    },
    )

# Signup page.
def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm( request.POST )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            full_name = form.cleaned_data.get('full_name')
            description = form.cleaned_data.get('description')

            f = open(os.path.join(settings.MEDIA_ROOT, 'registrations.txt'), 'a')
            f.write( str(timezone.now()) )
            f.write( str('\n') )
            f.write( str(username) )
            f.write( str('\n') )
            f.write( str(full_name) )
            f.write( str('\n') )
            f.write( str(description) )
            f.write( str('\n\n\n') )
            f.close()

            return redirect('index')

    return render(request, 'signup.html', {
        'form': form,
    },
    )

# Redirection view.
def redirection(request, short):
    try:
        # case insensitive matching
        url = URL.objects.get( short__iexact = short )
    except URL.DoesNotExist:
        raise Http404("Target URL not found.")

    url.clicks = url.clicks + 1
    url.save()

    from piwikapi.tracking import PiwikTracker
    from django.conf import settings
    piwiktracker = PiwikTracker(settings.PIWIK_SITE_ID, request)
    piwiktracker.set_api_url(settings.PIWIK_URL)
    piwiktracker.do_track_page_view('Redirect to %s' % url.target)

    return redirect( url.target )
