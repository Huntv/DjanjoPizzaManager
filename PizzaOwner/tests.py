from django.test import TestCase
from PizzaOwner.models import Topping

class ToppingModelTest(TestCase):

    def test_create_topping(self):
        topping = Topping.objects.create(name="Cheese")
        self.assertEqual(topping.name, "Cheese")
        self.assertEqual(str(topping), "Cheese")

    def test_topping_unique_name(self):
        Topping.objects.create(name="Cheese")
        with self.assertRaises(Exception):
            Topping.objects.create(name="Cheese")  # Should raise error because it's unique
