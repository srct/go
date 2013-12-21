from go.models import URL
from go.forms import URLForm
from datetime import timedelta
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Homepage view.
@login_required
def index(request):

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
            return redirect('success')

    return render(request, 'index.html', {
        'form': url_form,
    },
    )

# Sucessful url registration page.
@login_required
def success(request):

    url = None
    try:
        url = URL.objects.filter(owner=request.user).latest('date_created')
    except URL.DoesNotExist:
        pass

    return render(request, 'success.html', {
        'url': url,
    },
    )

# My-Links page.
@login_required
def my_links(request):
    links = URL.objects.filter( owner = request.user )

    return render(request, 'my_links.html', {
        'links' : links,
    },
    )

# Delete link page.
@login_required
def delete(request, short):
    url = get_object_or_404(URL, short = short )
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
    return render(request, 'signup.html', {

    },
    )

# Redirection view.
def redirection(request, short):
    try:
        # case insensitive matching
        url = URL.objects.get( short__iexact = short )
    except URL.DoesNotExist:
        raise Http404("Target URL not found.")

    target = url.target
    url.clicks = url.clicks + 1
    url.save()
    return redirect( target )
