from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('my/', views.my_orders, name='my_orders'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
]

# Register your models here.