"""Test case for shopper_profile."""


from django.test import TestCase
from .models import ShopperProfile, User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """User Factory class."""

    class Meta:
        """User class will be used."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    """Profile Factory class."""

    class Meta:
        """Shopper Profile class will be used."""

        model = ShopperProfile

    street = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    zip_code = factory.Faker('zipcode')
    cell = factory.Faker('phone_number')


class ProfileUnitTests(TestCase):
    """Profile Unit Test class."""

    @classmethod
    def setUpClass(cls):
        """Set up 50 fake user class instances."""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            profile = ProfileFactory.create(user=user)
            profile.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down class."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        """Test case for user object instance if it has profile."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)
