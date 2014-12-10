# -*- coding: utf-8 -*-
from django.db import models
from Course.models import Course
from dossier.models import Dossier


# Create your models here.
class Student(models.Model):
    course = models.ManyToManyField(Course, related_name='student_of_c')
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
    dossiers = models.OneToOneField(Dossier, related_name='student_of_d')

    def __str__(self):
        return self.surname + " " + self.name
