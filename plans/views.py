from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plan
from .serializers import PlanSerializer

@api_view(['POST'])
def modifyPlan(request):
    return 1

@api_view(['GET'])
def getAllPlans(request):
    allplans = PlanSerializer(Plan.objects.all(), many=True)
    return Response(allplans.data)