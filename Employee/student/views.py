from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializers
from .models import Student
from rest_framework import generics

# Create your views here.

class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all
    serializer_class = StudentSerializers
    
class StudentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
class StudentdeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
class StudentApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
