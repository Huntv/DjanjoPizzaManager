from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ Import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzaowner/', include('PizzaOwner.urls')),
    path('pizzachef/', include('PizzaChef.urls')),
    
    # Redirect `/` to `/pizzaowner/`
    path('', lambda request: redirect('topping_list', permanent=False)),  
]
