# -*- coding: utf-8 -*-
from django.db import models
from Coaches.models import Coach


class Course(models.Model):
    PY = 'python'
    LANG = (
        ('PY', 'python'),
        ('PHP', 'php'),
        ('JAVA', 'java'),
    )
    language = models.CharField(max_length=20, choices=LANG,
                                default=PY)
    name = models.CharField('Имя', max_length=25)
    teacher = models.ForeignKey(Coach, related_name='+')
    assistant = models.ForeignKey(Coach, related_name='+')
    data_start = models.DateField()
    data_finish = models.DateField()

    def __str__(self):
        return self.name
