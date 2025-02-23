from django.test import TestCase
from django.urls import reverse
from .models import Pizza
from PizzaOwner.models import Topping

class PizzaViewsTest(TestCase):

    def setUp(self):
        print("Setting up test data...")
        # Create toppings for use in tests
        self.topping1 = Topping.objects.create(name="Cheese")
        self.topping2 = Topping.objects.create(name="Pepperoni")
        # Create a pizza for testing update and delete
        self.pizza = Pizza.objects.create(name="Margherita")
        self.pizza.toppings.add(self.topping1)

    def test_pizza_list_view(self):
        print("Testing: Pizza List View")
        response = self.client.get(reverse('pizza_list'))  # Adjust to your URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Margherita")
        self.assertContains(response, "Cheese")
        self.assertContains(response, "Pepperoni")
        print("Passed: Pizza List View test passed")

    def test_pizza_create_view_success(self):
        print("Testing: Pizza Create View (success)")
        response = self.client.post(reverse('pizza_create'), {
            'name': 'Pepperoni Pizza',
            'toppings': [self.topping1.id, self.topping2.id]
        })
        self.assertRedirects(response, reverse('pizza_list'))

        # Check if the pizza was created
        try:
            pizza = Pizza.objects.get(name="Pepperoni Pizza")
            self.assertEqual(pizza.toppings.count(), 2)
            print("Passed: Pizza Create View (success) test passed")
        except Pizza.DoesNotExist:
            print("Failed: Pizza 'Pepperoni Pizza' was not created.")
            self.fail("Pizza 'Pepperoni Pizza' does not exist")


    def test_pizza_create_view_duplicate(self):
        print("Testing: Pizza Create View (duplicate name)")
        # Create a pizza with the same name
        response = self.client.post(reverse('pizza_create'), {
            'name': 'Margherita',
            'toppings': [self.topping2.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza &#x27;Margherita&#x27; already exists!")  # Ensure proper HTML encoding is handled
        print("Passed: Pizza Create View (duplicate name) test passed")

    def test_pizza_update_view_success(self):
        print("Testing: Pizza Update View (success)")
        response = self.client.post(reverse('pizza_update', kwargs={'pizza_id': self.pizza.id}), {
            'name': 'Updated Margherita',
            'toppings': [self.topping2.id]
        })
        self.assertRedirects(response, reverse('pizza_list'))
        self.pizza.refresh_from_db()
        self.assertEqual(self.pizza.name, "Updated Margherita")
        self.assertEqual(self.pizza.toppings.count(), 1)
        self.assertIn(self.topping2, self.pizza.toppings.all())
        print("Passed: Pizza Update View (success) test passed")

    def test_pizza_update_view_duplicate(self):
        print("Testing: Pizza Update View (duplicate name)")
        # Create another pizza and add toppings using add()
        pizza = Pizza.objects.create(name="Pepperoni Pizza")
        pizza.toppings.add(self.topping1)

        response = self.client.post(reverse('pizza_update', kwargs={'pizza_id': self.pizza.id}), {
            'name': 'Pepperoni Pizza',  # Duplicate name
            'toppings': [self.topping1.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza &#x27;Pepperoni Pizza&#x27; already exists!")  # Ensure proper HTML encoding is handled
        print("Passed: Pizza Update View (duplicate name) test passed")



    def test_pizza_delete_view(self):
        print("Testing: Pizza Delete View")
        response = self.client.post(reverse('pizza_delete', kwargs={'pizza_id': self.pizza.id}))
        self.assertRedirects(response, reverse('pizza_list'))
        # Check if the pizza is deleted
        with self.assertRaises(Pizza.DoesNotExist):
            Pizza.objects.get(id=self.pizza.id)
        print("Passed: Pizza Delete View test passed")
