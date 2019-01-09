"""
go/serializers.py

Define how data is translated from the database to json/API representation.
"""
# Third Party Imports
from rest_framework import serializers

# App Imports
from .models import URL


class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        lookup_field = "short"
        fields = ("destination", "short", "date_expires")

