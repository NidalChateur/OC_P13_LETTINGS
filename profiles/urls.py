from django.urls import path

from .views import index, profile

urlpatterns = [
    path("profiles/", index, name="profiles"),
    path("profiles/<str:username>/", profile, name="profile"),
]
