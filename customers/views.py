from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['GET'])
def getAllCustomers(request):
    allCustomersSerialized = CustomerSerializer(Customer.objects.all(), many=True)
    return Response(allCustomersSerialized.data)

@api_view(['GET'])
def getCustomerByPhoneNumber(request, phoneNumber):
    customersSerialized = CustomerSerializer(Customer.objects.get(phoneNumber = phoneNumber), many=False)
    return Response(customersSerialized.data)

@api_view(['POST'])
def createCustomer(request):
    customersSerializer = CustomerSerializer(data=request.data)
    if customersSerializer.is_valid():
        customersSerializer.save()
    return Response(customersSerializer.data)

@api_view(['POST'])
def updateCustomer(request, phoneNumber):
    customer = Customer.objects.get(phoneNumber = phoneNumber)
    customersSerializer = CustomerSerializer(instance=customer, data=request.data)
    
    if customersSerializer.is_valid():
        customersSerializer.save()
    
    return Response(customersSerializer.data)