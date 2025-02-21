from django.db import models
from PizzaOwner.models import Topping  # Import toppings from PizzaOwner

class Pizza(models.Model):
    name = models.CharField(max_length=100, unique=True)
    toppings = models.ManyToManyField(Topping)  # Many toppings per pizza

    def __str__(self):
        return self.name
