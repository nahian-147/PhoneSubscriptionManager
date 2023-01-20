from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('modify_plan/', views.modifyPlan, name='modify_plan'),
    path('get_all_plans/', views.getAllPlans, name='get_all_plans'),
]
