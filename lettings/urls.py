from django.urls import path

from .views import index, letting

urlpatterns = [
    path("lettings/", index, name="lettings"),
    path("lettings/<str:letting_id>/", letting, name="letting"),
]
