from django.urls import path, include

urlpatterns = [
    path('', include('go.urls')),
    path('', include('go_forward.urls')),
]
