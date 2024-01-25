from django.test import TestCase
from django.urls import resolve, reverse
from home.views import HomeView


class TestHomeUrl(TestCase):
    def setUp(self):
        self.url = reverse("home:main")

    def test_get_home_url(self):
        self.assertEquals(resolve(self.url).func.view_class,HomeView)