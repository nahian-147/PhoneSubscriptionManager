from django.db import models
from enum import Enum

class PlanNames(Enum):

    GLOBALNET_BRONZE = 'Globalnet Bronze'

    GLOBALNET_SILVER = 'Globalnet Silver'

    GLOBALNET_GOLD = 'Globalnet Gold'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Plan(models.Model):

    planName = models.CharField(max_length=20, choices=PlanNames.choices())
    subsciptionPricePerMonthInBDT = models.FloatField()
    subsciptionExpireInMonths = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.planName
 
 