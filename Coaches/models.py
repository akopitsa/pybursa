# -*- coding: utf-8 -*-
from django.db import models
from dossier.models import Dossier
from django.contrib.auth.models import User


class Coach(models.Model):
    ASSIST = 'assistant'
    T_OR_A = (
        ('TEACH', 'teacher'),
        ('ASSIST', 'assistant'),
    )
    teach_or_assist = models.CharField(max_length=15, choices=T_OR_A,
                                       default=ASSIST)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    us = models.ForeignKey(User)
    dos = models.OneToOneField(Dossier, related_name='coach_of')
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length='65')

    def __str__(self):
        return self.surname + " " + self.name
