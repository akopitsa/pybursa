# -*- coding: utf-8 -*-
from django.db import models
from coach.models import Coach
from address.models import Address


class Course(models.Model):
    LANG = (
        ('PYTHON', 'python'),
        ('PHP', 'php'),
        ('JAVA', 'java'),
        ('C#', 'c#'),
    )
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    teacher = models.ForeignKey(Coach, related_name='teacher')
    assist = models.ForeignKey(Coach, related_name='assist')
    start = models.DateTimeField()
    finish = models.DateTimeField()
    technology = models.CharField(max_length=15, choices=LANG)
    venue = models.ForeignKey(Address)
    slug = models.SlugField(max_length=45)

    def __unicode__(self):
        return self.technology
