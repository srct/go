"""
go/views.py

The functions that handle a request to a given URL. Get some data, manipulate
it, and return a rendered template.
"""
from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import URLSerializer
from .models import URL


class URLPermission(permissions.BasePermission):
    """Custom permission check on URL model operations."""

    message = "You do not have the necessary approvals to perform that action."

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user.registereduser


class URLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that handles creation/read/update/deletion of URL objects.
    """

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    serializer_class = URLSerializer
    permission_classes = (URLPermission, IsAuthenticated)
    lookup_field = "short"

    def get_queryset(self):
        return URL.objects.filter(owner=self.request.user.registereduser)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.registereduser)


class CustomAuthToken(ObtainAuthToken):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({"token": token.key})


class GetSessionInfo(APIView):
    """Handy endpoint to return current user session status & information to the frontend."""

    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=request.user)
        session_info = {
            "username": request.user.username,
            # "full_name": f"{request.user.get_full_name}",
            "last_login": request.user.last_login,
            "is_authenticated": request.user.is_authenticated,
            "token": token.key,
        }
        return Response(session_info)


def redirection(request, short):
    """
    This view redirects a user based on the short URL they requested.
    """
    # Get the URL object that relates to the requested Go link
    url = get_object_or_404(URL, short__iexact=short)

    return redirect(url.destination)
