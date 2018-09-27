"""
go/views.py

The functions that handle a request to a given URL. Get some data, manipulate
it, and return a rendered template.
"""
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import URLSerializer
from .models import URL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class URLPermission(permissions.BasePermission):
    """Custom permission check on URL model operations."""

    message = "You do not have the necessary approvals to perform that action."

    def has_permission(self, request, view):
        return request.user.registereduser.approved or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user.registereduser or request.user.is_staff


class URLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that handles creation/read/update/deletion of URL objects.
    """

    authentication_classes = (TokenAuthentication,)
    serializer_class = URLSerializer
    permission_classes = (URLPermission, IsAuthenticated)
    lookup_field = "short"

    def get_queryset(self):
        if not self.request.user.is_staff:
            return URL.objects.filter(owner=self.request.user.registereduser)
        return URL.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.registereduser)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({"token": token.key})

