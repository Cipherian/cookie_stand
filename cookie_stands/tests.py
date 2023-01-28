from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import CookieStand


class CookieStandTests(TestCase):
    # TODO: test your app

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.cookie = CookieStand.objects.create(
            location='Chips', description='tasty', owner=self.user, hourly_sales={'key': 'value'}, minimum_customers_per_hour=5, maximum_customers_per_hour=6, average_cookies_per_sale=2.5)

    def test_string_representation(self):
        self.assertEqual(str(self.cookie), 'Chips')

    def test_movie_location(self):
        self.assertEqual(f'{self.cookie.location}', 'Chips')

    def test_movie_rating(self):
        self.assertEqual(f'{self.cookie.description}', 'tasty')

    def test_hourly_sales(self):
        self.assertEqual(f'{self.cookie.hourly_sales}', "{'key': 'value'}")

    def test_minimum_customers_per_hour(self):
        self.assertEqual(f'{self.cookie.minimum_customers_per_hour}', '5')

    def test_maximum_customers_per_hour(self):
        self.assertEqual(f'{self.cookie.maximum_customers_per_hour}', '6')

    def test_average_cookies_per_sale(self):
        self.assertEqual(f'{self.cookie.average_cookies_per_sale}', '2.5')

    # def test_list_page_status_code(self):
    #     url = reverse("thing_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_list_page_template(self):
    #     url = reverse("thing_list")
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, "home.html")
    #     self.assertTemplateUsed(response, "cookie_list.html")
