from django.urls import resolve, reverse

from lettings.views import index, letting


class TestUrls:
    def test_lettings_url(self):
        # 1. path test
        assert reverse("lettings") == "/lettings/"

        # 2. url name test
        assert resolve("/lettings/").view_name == "lettings"

        # 3. view name test
        assert resolve("/lettings/").func is index

    def test_letting_url(self):
        # 1. path test
        assert reverse("letting", args=[1]) == "/lettings/1/"

        # 2. url name test
        assert resolve("/lettings/1/").view_name == "letting"

        # 3. view name test
        assert resolve("/lettings/1/").func is letting
