from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToppingListView.as_view(), name='topping_list'),  
    path('create/', views.ToppingCreateView.as_view(), name='topping_create'),  
    path('update/<int:topping_id>/', views.ToppingUpdateView.as_view(), name='topping_update'),  
    path('delete/<int:topping_id>/', views.ToppingDeleteView.as_view(), name='topping_delete'),  
]
