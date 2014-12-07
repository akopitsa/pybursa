# -*- coding: utf-8 -*-
from django.db import models


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

    def __str__(self):
        return self.surname + " " + self.name
