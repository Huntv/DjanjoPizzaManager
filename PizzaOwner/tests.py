from django.test import TestCase
from django.urls import reverse
from django.db import IntegrityError
from PizzaOwner.models import Topping

class ToppingModelTest(TestCase):

    def test_create_topping(self):
        print("Testing: Create a topping")
        response = self.client.post(reverse('topping_create'), {'name': 'Cheese'})
        # Check if the Topping was created successfully
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertTrue(Topping.objects.filter(name="Cheese").exists())
        print("Passed: Topping created successfully")

    def test_create_duplicate_topping(self):
        print("Testing: Create duplicate topping name")
        Topping.objects.create(name="Cheese")
        response = self.client.post(reverse('topping_create'), {'name': 'Cheese'})
    
        # Check if the response code is 200 (should not redirect)
        self.assertEqual(response.status_code, 200)  
    
        # Match the HTML-encoded error message
        self.assertContains(response, "Topping &#x27;Cheese&#x27; already exists")  # Match the encoded message
        print("Passed: Duplicate create test passed")


    def test_topping_list_view(self):
        print("Testing: Topping list view")
        Topping.objects.create(name="Cheese")
        response = self.client.get(reverse('topping_list'))
        # Check if the list of toppings is rendered correctly
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cheese")
        print("Passed: Topping list view test passed")

    def test_update_topping(self):
        print("Testing: Update a topping")
        topping = Topping.objects.create(name="Cheese")
        response = self.client.post(reverse('topping_update', kwargs={'topping_id': topping.id}), {'name': 'Mozzarella'})
        # Check if the topping was updated
        topping.refresh_from_db()
        self.assertEqual(topping.name, "Mozzarella")
        self.assertEqual(response.status_code, 302)  # Should redirect after update
        print("Passed: Topping updated successfully")

    def test_update_duplicate_topping(self):
        print("Testing: Update to a duplicate topping name")
        topping1 = Topping.objects.create(name="Cheese")
        topping2 = Topping.objects.create(name="Pepperoni")
        response = self.client.post(reverse('topping_update', kwargs={'topping_id': topping1.id}), {'name': 'Pepperoni'})
        # Check for error message when trying to set a duplicate name
        self.assertEqual(response.status_code, 200)  # Should stay on the page (not redirect)
        self.assertContains(response, "Topping &#x27;Pepperoni&#x27; already exists")  # Match the encoded message
        print("Passed: Duplicate update test passed")


    def test_delete_topping(self):
        print("Testing: Delete a topping")
        topping = Topping.objects.create(name="Cheese")
        response = self.client.post(reverse('topping_delete', kwargs={'topping_id': topping.id}))
        # Check if the topping is deleted
        with self.assertRaises(Topping.DoesNotExist):
            Topping.objects.get(id=topping.id)
        self.assertEqual(response.status_code, 302)  # Should redirect after delete
        print("Passed: Topping deleted successfully")
