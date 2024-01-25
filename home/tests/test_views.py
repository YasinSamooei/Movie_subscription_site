from django.test import Client, TestCase
from django.urls import reverse
from accounts.models import User


class TestHomeUrl(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("home:main")
        self.user = User.objects.create(email="test@gmail.com", password="1234test")

    def test_get_home_with_out_login(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)

    def test_get_home_with_login(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
