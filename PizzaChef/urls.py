from django.urls import path
from . import views

urlpatterns = [
    path('', views.PizzaListView.as_view(), name='pizza_list'),
    path('create/', views.PizzaCreateView.as_view(), name='pizza_create'),
    path('update/<int:pizza_id>/', views.PizzaUpdateView.as_view(), name='pizza_update'), 
    path('delete/<int:pizza_id>/', views.PizzaDeleteView.as_view(), name='pizza_delete'),
]
