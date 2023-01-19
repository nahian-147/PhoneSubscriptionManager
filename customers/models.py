from django.db import models
from plans.models import Plan

class Customer(models.Model):
    name = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=14,primary_key=True)
    email = models.CharField(max_length=60)
    signUpDate = models.DateField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    subscriptionStartDateTime = models.DateTimeField()
    totalBill = models.FloatField()
    