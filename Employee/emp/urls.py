from django.urls import path
from .views import *

urlpatterns = [
    
    path('create/', EmployeeCreteApi.as_view()),
    path('update/<int:pk>/', EmployeeUpdateApi.as_view()),
    path('delete/<int:pk>/', EmployeedeleteApi.as_view()),
    path('api/', EmployeeApi.as_view()),
]
