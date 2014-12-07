# -*- coding: utf-8 -*-
from django.db import models
from Course.models import Course


# Create your models here.
class Student(models.Model):
    course = models.ForeignKey(Course)
    STD = 'standart'
    PACKAGES = (
        ('STD', 'standart'),
        ('VIP', 'vip'),
        ('GOLD', 'gold'),
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15, choices=PACKAGES,
                               default=STD)

    def __str__(self):
        return self.surname + " " + self.name
