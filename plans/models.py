from django.db import models
import enum

class PlanNames(enum.Enum):

    GLOBALNET_BRONZE = 'Globalnet Bronze'

    GLOBALNET_SILVER = 'Globalnet Silver'

    GLOBALNET_GOLD = 'Globalnet Gold'


class Plan(models.Model):

    planName = models.CharField(choices=PlanNames.choices)
    subsciptionPricePerMonthInBDT = models.FloatField()
    subsciptionDurationInMonths = models.IntegerField()
 