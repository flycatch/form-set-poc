from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    establish_year = models.IntegerField()
    founder = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    register_date = models.DateField(auto_now_add=True)
    CLIENT_CHOICES = (
        ('Domestic', 'Domestic'),
        ('International', 'International'),
    )
    type = models.CharField(max_length=200, choices=CLIENT_CHOICES)
    SYS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    sys_type = models.CharField(max_length=15, choices=SYS_CHOICES)
    project_name = models.CharField("Project Name", max_length=100)
    system_parameter_one = models.CharField(max_length=100)
    system_parameter_two = models.CharField(max_length=100)