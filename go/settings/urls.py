"""
settings/urls.py
"""
from django.urls import path, include

urlpatterns = [path("", include("go_back.urls")), path("", include("go_ahead.urls"))]
