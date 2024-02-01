import pytest
from django.conf import settings
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from home import views

# from tests import Mock

# client = Client()


# class TestView(Mock):
class TestView:
    client = Client()

    def test_index(self):
        response = self.client.get(reverse("home"))
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")

    def test_404(self, monkeypatch):
        """test 404 error : page not found"""

        # to keep clean sentry issues we path the log
        monkeypatch.setattr(views, "add_log", lambda *args, **kwargs: None)

        settings.DEBUG = False
        assert settings.DEBUG is False

        response = self.client.get("/inexistant_path/")
        assert response.status_code == 404
        assertTemplateUsed(response, "404.html")

    def test_check_500(self, monkeypatch):
        """test 500 error : internal server error"""

        # to keep clean sentry issues we path the log
        monkeypatch.setattr(views, "add_log", lambda *args, **kwargs: None)

        settings.DEBUG = False
        assert settings.DEBUG is False

        # settings.TEST = True
        # assert settings.TEST is True

        with pytest.raises(expected_exception=ValueError):
            response = self.client.get(reverse("check_500"))
            assert response.status_code == 500
            assertTemplateUsed(response, "500.html")

    def test_503(self):
        """test 503 error : service unavailable for maintenance"""

        settings.MAINTENANCE_MODE = True
        assert settings.MAINTENANCE_MODE is True

        response = self.client.get(reverse("home"))
        assert response.status_code == 503
        assertTemplateUsed(response, "503.html")
