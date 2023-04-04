from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import Employee
from rest_framework import generics

# Create your views here.

class EmployeeCreteApi(generics.CreateAPIView):
    queryset = Employee.objects.all
    serializer_class = EmployeeSerializer
    
class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeedeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer
    

