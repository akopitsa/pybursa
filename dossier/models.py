from django.db import models
from address.models import Address
from Course.models import Course

# Create your models here.


class Dossier(models.Model):
    COLORS = (
        ('RED', 'red'),
        ('WHITE', 'white'),
        ('BLACK', 'black'),
        ('YELLOW', 'yellow'),
        ('GREEN', 'green'),
        ('BLUE', 'blue'),
        ('GREY', 'grey'),
    )
    addr = models.ForeignKey(Address, related_name='dossier_of')
    unlikecourse = models.ManyToManyField(Course, related_name='dossier_of')
    color = models.CharField(max_length=25, choices=COLORS)
