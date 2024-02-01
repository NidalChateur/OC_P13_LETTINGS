from django.urls import path

from .views import check_500, index

urlpatterns = [
    path("", index, name="home"),
    path("check_500/", check_500, name="check_500"),
]
