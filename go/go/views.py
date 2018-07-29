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
from .serializers import URLSerializer

class URLPermission(permissions.BasePermission):
    message = "You do not have the necessary approvals to perform that action."
    def has_permission(self, request, view):
        return request.user.registereduser.approved or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user.registereduser or request.user.is_staff

class URLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that handles creation/read/update/deletion of URL objects.
    """
    serializer_class = URLSerializer
    permission_classes = (URLPermission,)
    lookup_field = 'short'

    def get_queryset(self):
        if not self.request.user.is_staff:
            return URL.objects.filter(owner=self.request.user.registereduser)
        else:
            return URL.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.registereduser)
