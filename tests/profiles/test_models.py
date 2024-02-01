# pylint: disable=no-member
import pytest

from profiles.models import Profile, User


class TestProfile:
    model = Profile

    @pytest.mark.django_db
    def test_str(self):
        profile_1 = self.model.objects.get(id=1)

        assert str(profile_1) == profile_1.user.username

    @pytest.mark.parametrize(
        "favorite_city, user_id",
        [
            ("Buenos Aires", 5),
            ("Barcelona", 4),
            ("Budapest", 3),
            ("Berlin", 2),
        ],
    )
    @pytest.mark.django_db
    def test_instances_presence_in_db(
        self,
        favorite_city: str,
        user_id: int,
    ):
        profile = self.model.objects.filter(
            favorite_city=favorite_city,
            user_id=User.objects.get(id=user_id),
        )
        assert len(profile) == 1

    @pytest.mark.django_db
    def test_number_of_instances(self):
        assert len(self.model.objects.all()) == 4
