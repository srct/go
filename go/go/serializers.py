"""
go/serializers.py

Define how data is translated from the database to json/API representation.
"""
# Django Imports
from django.contrib.auth.models import User, Group

# App Imports
from .models import URL, RegisteredUser

# Third Party Imports
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name',
                  'last_name', 'is_staff')

class RegisteredUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = '__all__'

class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
