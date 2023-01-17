from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'password': 'bMvnu2?!20',
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
