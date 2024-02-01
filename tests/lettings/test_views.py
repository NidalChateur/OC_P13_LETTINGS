# pylint: disable=no-member
import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from lettings import views
from lettings.models import Letting

# from tests import Mock

client = Client()


# class TestView(Mock):
class TestView:
    client = Client()

    @pytest.mark.django_db
    def test_index(self):
        # 1. test success
        response = self.client.get(reverse("lettings"))
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_letting(self, monkeypatch):
        # to keep clean sentry issues we path the log
        monkeypatch.setattr(views, "add_log", lambda *args, **kwargs: None)

        # 1. test success
        response = self.client.get(reverse("letting", args=[1]))
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")

        # 2. test Letting.DoesNotExist (int)
        letting_id = 9999
        assert Letting.objects.filter(id=letting_id).count() == 0
        response2 = self.client.get(reverse("letting", args=[letting_id]))
        assert response2.status_code == 200
        assertTemplateUsed(response2, "404.html")
        error = f"Letting.DoesNotExist : Letting id n°{letting_id} does not exist !"
        assert error in response2.content.decode()

        # 3. test ValueError (str)
        letting_id = "inexistant"
        response3 = self.client.get(reverse("letting", args=[letting_id]))
        assert response3.status_code == 200
        assertTemplateUsed(response3, "404.html")
        error = f"ValueError : Field id expected a number but got {letting_id}"
        assert error in response3.content.decode()
