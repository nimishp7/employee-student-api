from django.db import models

# Create your models here.

class Student(models.Model):
    stu_reg = models.TextField(unique=True)
    stu_name = models.TextField()
    stu_email = models.EmailField()
    stu_mo = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)