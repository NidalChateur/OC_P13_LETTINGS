from django.urls import resolve, reverse

from profiles.views import index, profile


class TestUrls:
    def test_profiles_url(self):
        # 1. path test
        assert reverse("profiles") == "/profiles/"

        # 2. url name test
        assert resolve("/profiles/").view_name == "profiles"

        # 3. view name test
        assert resolve("/profiles/").func is index

    def test_profile_url(self):
        # 1. path test
        assert reverse("profile", args=[1]) == "/profiles/1/"

        # 2. url name test
        assert resolve("/profiles/1/").view_name == "profile"

        # 3. view name test
        assert resolve("/profiles/1/").func is profile
