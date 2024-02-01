from django.urls import resolve, reverse

from home import urls
from home.urls import check_500
from home.views import index

# from tests import Mock


# class TestUrls(Mock):
class TestUrls:
    def test_index_url(self):
        # 1. path test
        assert reverse("home") == "/"

        # 2. url name test
        assert resolve("/").view_name == "home"

        # 3. view name test
        assert resolve("/").func is index

    def test_check_500(self, monkeypatch):
        # to keep clean sentry issues we path the check_500 view
        monkeypatch.setattr(urls, "check_500", lambda *args, **kwargs: None)

        # 1. path test
        assert reverse("check_500") == "/check_500/"

        # 2. url name test
        assert resolve("/check_500/").view_name == "check_500"

        # 3. view name test
        assert resolve("/check_500/").func is check_500
