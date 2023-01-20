from django.contrib import admin
from .models import Customer, Company, LastAssignedPhoneNumberSuffix

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(LastAssignedPhoneNumberSuffix)