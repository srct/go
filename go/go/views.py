"""
go/views.py

The functions that handle a request to a given URL. Get some data, manipulate
it, and return a rendered template.
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
from .forms import EditForm, SignupForm, URLForm
from .models import URL, RegisteredUser


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, URLSerializer, RegisteredUserSerializer

class CrudPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user.registereduser or request.user.is_staff

class RegisteredUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RegisteredUsers to be viewed or edited.
    """
    queryset = RegisteredUser.objects.all()
    serializer_class = RegisteredUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class URLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that handles creation/read/update/deletion of URL objects.
    """
    serializer_class = URLSerializer
    queryset = URL.objects.all()
