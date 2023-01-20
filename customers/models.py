from django.db import models
from plans.models import Plan
from enum import Enum

class ownerTypes(Enum):

    PERSONAL = 'personal'
    COMPANY = 'company'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Company(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    
    name = models.CharField(max_length=250)
    primaryPhoneNumber = models.CharField(max_length=14,primary_key=True)
    email = models.CharField(max_length=60)
    signUpDate = models.DateField()
    ownerType = models.CharField(max_length=15, choices=ownerTypes.choices(), default=ownerTypes.PERSONAL)
    
    company = models.ForeignKey(Company,default=None, null=True,blank=True, on_delete=models.SET_NULL)
    # otherPhoneNumbers = models.ListCharField(
    #     base_field = models.CharField(max_length=14),
    #     size=3,
    #     max_length=(3 * 15),
    # )
    
    plan = models.ForeignKey(Plan,default=None, null=True,blank=True, on_delete=models.SET_NULL)
    subscriptionStartDateTime = models.DateTimeField(default=None, null=True,blank=True)
    
    totalBill = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.name + ' ' + self.primaryPhoneNumber


class LastAssignedPhoneNumberSuffix(models.Model):
    
    number = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.number