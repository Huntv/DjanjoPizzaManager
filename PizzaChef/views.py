from django.shortcuts import render, redirect
from django.views import View
from .models import Pizza
from PizzaOwner.models import Topping  # Import toppings

class PizzaListView(View):
    def get(self, request):
        pizzas = Pizza.objects.all()
        toppings = Topping.objects.all()  # Get available toppings
        return render(request, 'pizzachef/index.html', {'pizzas': pizzas, 'toppings': toppings})

class PizzaCreateView(View):
    def post(self, request):
        name = request.POST.get('name').strip()
        topping_ids = request.POST.getlist('toppings')  # Get selected toppings
        if name:
            if Pizza.objects.filter(name__iexact=name).exists():
                pizzas = Pizza.objects.all()
                toppings = Topping.objects.all()
                return render(request, 'pizzachef/index.html', {
                    'pizzas': pizzas,
                    'toppings': toppings,
                    'error_message': f"Pizza '{name}' already exists!"
                })
            else:
                pizza = Pizza.objects.create(name=name.capitalize())  # Save name with capitalization
                pizza.toppings.set(Topping.objects.filter(id__in=topping_ids))  # Assign toppings
        return redirect('pizza_list')

class PizzaUpdateView(View):
    def post(self, request, pizza_id):
        name = request.POST.get('name', '').strip()
        topping_ids = request.POST.getlist('toppings')

        pizza = Pizza.objects.get(id=pizza_id)

        # Check for duplicate pizza names only if a new name is provided
        if name and Pizza.objects.filter(name__iexact=name).exclude(id=pizza_id).exists():
            pizzas = Pizza.objects.all()
            toppings = Topping.objects.all()
            return render(request, 'pizzachef/index.html', {
                'pizzas': pizzas,
                'toppings': toppings,
                'error_message': f"Pizza '{name}' already exists!",
            })

        # Update pizza name only if a new name is provided
        if name:
            pizza.name = name.capitalize()

        # Update toppings
        pizza.toppings.set(Topping.objects.filter(id__in=topping_ids))
        pizza.save()

        return redirect('pizza_list')


class PizzaDeleteView(View):
    def post(self, request, pizza_id):
        pizza = Pizza.objects.get(id=pizza_id)
        pizza.delete()
        return redirect('pizza_list')
