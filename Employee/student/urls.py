from django.urls import path
from .views import *

urlpatterns = [
    # path('api', EmployeeApi.as_view()),
    path('create/', StudentCreateApi.as_view()),
    path('update/<int:pk>/', StudentUpdateApi.as_view()),
    path('delete/<int:pk>/', StudentdeleteApi.as_view()),
    path('api/', StudentApi.as_view()),
]
