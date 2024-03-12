from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu, Booking


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu.save()

    def test_get_all(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "IceCream")
        self.assertEqual(response.data[0]["price"], "80.00")
        self.assertEqual(response.data[0]["inventory"], 100)
