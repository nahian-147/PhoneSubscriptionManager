from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('update_customer/<str:phoneNumber>', views.updateCustomer, name='update_customer'),
    path('get_all_customers/', views.getAllCustomers, name='get_all_customers'),
    path('get_customer/<str:phoneNumber>', views.getCustomerByPhoneNumber, name='get_customer'),
     path('change_plan/<str:phoneNumber>', views.changePlan, name='change_plan'),
    
]
