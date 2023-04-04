from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_regno = models.TextField(unique=True)
    emp_name = models.TextField()
    emp_email = models.EmailField()
    emp_mo = models.TextField()
    created_at = models.DateTimeField(auto_now=True)