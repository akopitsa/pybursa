# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    TYPE = (
        ('TEACHER', 'teacher'),
        ('ASSISTANT', 'assistant')
    )
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=55)
    email = models.CharField(max_length=65)
    phone = models.CharField(max_length=45)
    type = models.CharField(max_length=15, choices=TYPE)
    usrs = models.ForeignKey(User, verbose_name=u'Пользователь')
    dossier = models.OneToOneField('student.Dossier', blank=True, null=True)

    class Meta:
        verbose_name = 'ТРЕНЕРА'

    def __unicode__(self):
        return "%s %s (%s)" % (self.name, self.surname, self.type)
