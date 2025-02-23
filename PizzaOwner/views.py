from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Topping

class ToppingListView(View): #Renders the entire topping list from the database
    def get(self, request):
        toppings = Topping.objects.all()
        return render(request, 'PizzaOwner/index.html', {'toppings': toppings})

class ToppingCreateView(View):
    def post(self, request):
        name = request.POST.get('name').strip()  # Remove extra spaces
        if name:
            if Topping.objects.filter(name__iexact=name).exists():
                # ✅ Show an error message if the topping already exists (case-insensitive)
                toppings = Topping.objects.all()
                return render(request, 'PizzaOwner/index.html', {
                    'toppings': toppings,
                    'error_message': f"Topping '{name}' already exists (case-insensitive)!"
                })
            else:
                Topping.objects.create(name=name.title())  # Store with first letter capitalized
        return redirect('topping_list')

class ToppingUpdateView(View):
    def post(self, request, topping_id):
        name = request.POST.get('name').strip()
        if name:
            if Topping.objects.filter(name__iexact=name).exclude(id=topping_id).exists():
                toppings = Topping.objects.all()
                return render(request, 'PizzaOwner/index.html', {
                    'toppings': toppings,
                    'error_message': f"Topping '{name}' already exists (case-insensitive)!",
                })
            else:
                topping = Topping.objects.get(id=topping_id)
                topping.name = name.title()  
                topping.save()
        return redirect('topping_list')


class ToppingDeleteView(View):
    def post(self, request, topping_id):
        topping = get_object_or_404(Topping, id=topping_id)
        topping.delete()
        return redirect('topping_list')
