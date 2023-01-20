import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer,LastAssignedPhoneNumberSuffix,Company
from plans.models import Plan
from .serializers import CustomerSerializer
from .phoneNumber import assignNewPhoneNumber

@api_view(['GET'])
def getAllCustomers(request):
    allCustomersSerialized = CustomerSerializer(Customer.objects.all(), many=True)
    return Response(allCustomersSerialized.data)

@api_view(['GET'])
def getCustomerByPhoneNumber(request, phoneNumber):
    customersSerialized = CustomerSerializer(Customer.objects.get(primaryPhoneNumber = phoneNumber), many=False)
    return Response(customersSerialized.data)

@api_view(['POST'])
def createCustomer(request):
    customer = request.data
    suffix = LastAssignedPhoneNumberSuffix.objects.all()[0]
    lastPhoneNumberSuffix=suffix.number
    customerRecord = Customer()
    customerRecord.primaryPhoneNumber = assignNewPhoneNumber(lastPhoneNumberSuffix)
    customerRecord.name = customer['name']
    customerRecord.email = customer['email']
    customerRecord.signUpDate = customer['signUpDate']
    customerRecord.ownerType = customer['ownerType']

    if 'subscriptionStartDateTime' in customer:
        customerRecord.subscriptionStartDateTime = customer['subscriptionStartDateTime']
    if 'company' in customer:
        customerRecord.company = Company.objects.get(pk=customer['company'])

    if 'plan' in customer:
        customerRecord.plan = Plan.objects.get(pk=customer['plan'])
        customerRecord.totalBill = customerRecord.plan.subsciptionPricePerMonthInBDT

    suffix.number = customerRecord.primaryPhoneNumber[-8:]
    suffix.save()
    
    customerRecord.save()
        
    return Response(CustomerSerializer(customerRecord).data)

@api_view(['POST'])
def updateCustomer(request, phoneNumber):
    customer = Customer.objects.get(primaryPhoneNumber = phoneNumber)
    customersSerializer = CustomerSerializer(instance=customer, data=request.data)
    
    if customersSerializer.is_valid():
        customersSerializer.save()
    
    return Response(customersSerializer.data)


@api_view(['POST'])
def changePlan(request, phoneNumber):
    customer = Customer.objects.get(primaryPhoneNumber = phoneNumber)
    requestedPlanId = request.data['id']
    plan = Plan.objects.get(pk=requestedPlanId)
    customer.plan = plan

    customer.save()
    
    return Response(CustomerSerializer(customer).data)

# def customerObjectFromCustomerDictionary(customerDictionary):
#     customerObject = Customer()