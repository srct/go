from go.models import URL
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Homepage view.
@login_required
def index(request):
    return render(request, 'index.html', {

    },
    )

# My-Links page.
@login_required
def my_links(request, permission = True):
    links = URL.objects.filter( owner = request.user )

    return render(request, 'my_links.html', {
        'links' : links,
        'permission' : permission,
    },
    )

# Delete link page.
@login_required
def delete(request, short):
    url = URL.objects.get( short = short )
    if url.owner == request.user:
        url.delete()
        return redirect('my_links')
    else:
        return my_links(request, permission = False)

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
        url = URL.objects.get( short = short )
    except URL.DoesNotExist:
        raise Http404("Target URL not found.")

    target = url.target
    url.clicks = url.clicks + 1
    url.save()
    return redirect( target )
