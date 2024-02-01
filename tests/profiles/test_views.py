# pylint: disable=no-member
import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from profiles import views
from profiles.models import Profile

# from tests import Mock

client = Client()


# class TestView(Mock):
class TestView:
    client = Client()

    @pytest.mark.django_db
    def test_index(self):
        # 1. test success
        response = self.client.get(reverse("profiles"))
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_profile(self, monkeypatch):
        # to keep clean sentry issues we path the log
        monkeypatch.setattr(views, "add_log", lambda *args, **kwargs: None)

        # 1. test success
        response = self.client.get(reverse("profile", args=["4meRomance"]))
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")

        # 2. test Profile.DoesNotExist
        username = "inexistant"
        assert Profile.objects.filter(user__username=username).count() == 0
        response2 = self.client.get(reverse("profile", args=[username]))
        assert response2.status_code == 200
        assertTemplateUsed(response2, "404.html")
        error = f"Profile.DoesNotExist : User with username {username} does not exist !"
        assert error in response2.content.decode()
