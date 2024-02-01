# pylint: disable=no-member
import pytest

from lettings.models import Address, Letting


class TestAddress:
    model = Address

    @pytest.mark.django_db
    def test_str(self):
        address_1 = self.model.objects.get(id=1)

        assert str(address_1) == f"{address_1.number} {address_1.street}"

    @pytest.mark.parametrize(
        "number, street, city, state, zip_code",
        [
            (
                7217,
                "Bedford Street",
                "Brunswick",
                "GA",
                31525,
            ),
            (
                4,
                "Military Street",
                "Willoughby",
                "OH",
                44094,
            ),
            (
                340,
                "Wintergreen Avenue",
                "Newport News",
                "VA",
                23601,
            ),
            (
                9230,
                "E. Joy Ridge Street",
                "Marquette",
                "MI",
                49855,
            ),
            (
                9606,
                "Harvard Street",
                "Aliquippa",
                "PA",
                15001,
            ),
            (
                588,
                "Argyle Avenue",
                "East Meadow",
                "NY",
                11554,
            ),
        ],
    )
    @pytest.mark.django_db
    def test_instances_presence_in_db(
        self,
        number: int,
        street: str,
        city: str,
        state: str,
        zip_code: int,
    ):
        address = self.model.objects.filter(
            number=number,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            country_iso_code="USA",
        )
        assert len(address) == 1

    @pytest.mark.django_db
    def test_number_of_instances(self):
        assert len(self.model.objects.all()) == 6


class TestLetting:
    model = Letting

    @pytest.mark.django_db
    def test_str(self):
        letting_1 = self.model.objects.get(id=1)

        assert str(letting_1) == letting_1.title

    @pytest.mark.parametrize(
        "title, address_id",
        [
            ("Joshua Tree Green Haus /w Hot Tub", 1),
            ("Oceanview Retreat", 2),
            ("'Silo Studio' Cottage", 3),
            ("Pirates of the Caribbean Getaway", 4),
            ("The Mushroom Dome Retreat & LAND of Paradise Suite", 5),
        ],
    )
    @pytest.mark.django_db
    def test_instances_presence_in_db(self, title: str, address_id: int):
        letting = self.model.objects.filter(
            title=title, address=Address.objects.get(id=address_id)
        )
        assert len(letting) == 1

    @pytest.mark.django_db
    def test_number_of_instances(self):
        assert len(self.model.objects.all()) == 6
