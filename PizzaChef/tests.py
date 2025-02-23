from django.test import TestCase
from PizzaOwner.models import Topping
from PizzaChef.models import Pizza

class PizzaModelTest(TestCase):

    def test_create_pizza(self):
        topping1 = Topping.objects.create(name="Cheese")
        topping2 = Topping.objects.create(name="Pepperoni")
        pizza = Pizza.objects.create(name="Cheese Pizza")
        pizza.toppings.set([topping1, topping2])

        # Test that pizza has the correct toppings
        self.assertIn(topping1, pizza.toppings.all())
        self.assertIn(topping2, pizza.toppings.all())
        self.assertEqual(pizza.name, "Cheese Pizza")
        self.assertEqual(str(pizza), "Cheese Pizza")
