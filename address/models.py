from django.db import models

# Create your models here.


class Address(models.Model):
    index = models.CharField(max_length=35)
    country = models.CharField(max_length=55)
    oblast = models.CharField(max_length=75)
    district = models.CharField(max_length=75)
    street = models.CharField(max_length=75)
    house = models.CharField(max_length=75)
