from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

from app.user.models import Account


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': 'passw0rd',
            'password2': 'passw0rd',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()