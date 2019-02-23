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
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import (
    URLSerializer,
    RegisteredUserSerializerForAdmins,
    RegisteredUserSerializerForUsers,
)
from .models import URL, RegisteredUser


class URLPermission(permissions.BasePermission):
    """Custom permission check on URL model operations."""

    message = "You do not have the necessary permission to perform that action on that URL object."

    def has_permission(self, request, view):
        """Has permission to interact with URL, the model"""
        return True

    def has_object_permission(self, request, view, obj):
        """Has permission to interact with a specific URL object"""
        return obj.owner == request.user.registereduser


class RegisteredUserPermission(permissions.BasePermission):
    """
    Custom permission check such that users can only modify their registered status and admins can control all of their statuses.
    """

    message = "You do not have the necessary permission to perform that action on that RegisteredUser object."

    def has_permission(self, request, view):
        """Has permission to interact with RegisteredUser, the model"""
        return True

    def has_object_permission(self, request, view, obj):
        """Has permission to interact with a specific RegisteredUser object"""
        return obj.user == request.user


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


class RegisteredUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for modifying RegisteredUser attributes.
    """

    authentication_classes = (SessionAuthentication,)
    permission_classes = (RegisteredUserPermission, IsAuthenticated)

    def get_queryset(self):
        return RegisteredUser.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return RegisteredUserSerializerForAdmins
        return RegisteredUserSerializerForUsers


class CustomAuthToken(ObtainAuthToken):
    """
    Custom endpoint to provide the currently logged in user's API token.
    """

    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({"token": token.key})


class GetSessionInfo(APIView):
    """Handy endpoint to return current user session status & information to the frontend."""

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        if not request.user.is_anonymous:
            session_info = {
                "user_id": request.user.id,
                "username": request.user.username,
                "is_authenticated": request.user.is_authenticated,
                "is_registered": request.user.registereduser.registered,
                "is_approved": request.user.registereduser.approved,
                "is_blocked": request.user.registereduser.blocked,
            }
        else:
            session_info = {
                "user_id": request.user.id,
                "username": request.user.username,
                "is_authenticated": request.user.is_authenticated,
            }
        return Response(session_info)


def redirection(request, short):
    """
    This view redirects a user based on the short URL they requested.

    The meat and potatoes of Go.
    """
    # Get the URL object that relates to the requested Go link
    url = get_object_or_404(URL, short__iexact=short)

    return redirect(url.destination)
