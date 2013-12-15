from go.models import URL
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Homepage view.
def index(request):
    return render(request, 'index.html', {

    },
    )

# About page, static.
def about(request):
    return render(request, 'about.html', {

    },
    )
