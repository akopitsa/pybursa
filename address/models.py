# -*- coding: utf-8 -*-
from django.db import models

class Address(models.Model):
    postindex = models.CharField(max_length=7)
    country = models.CharField(max_length=55)
    obl = models.CharField(max_length=55)
    district = models.CharField(max_length=55)
    street = models.CharField(max_length=55)
    house = models.CharField(max_length=6)

    def __unicode__(self):
        return "%s %s, %s, %s %s" % (self.postindex, self.country.upper(), self.obl,
                                     self.street, self.house)
