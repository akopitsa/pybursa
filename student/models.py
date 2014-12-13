from django.db import models
from address.models import Address
from course.models import Course


class Student(models.Model):
    PACKAGES = (
        ('STANDART', 'standart'),
        ('VIP', 'vip'),
        ('GOLD', 'gold')
    )
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    email = models.EmailField(max_length=76)
    phone = models.CharField(max_length=17)
    package = models.CharField(max_length=8, choices=PACKAGES)
    dossier = models.OneToOneField('Dossier', blank=True, null=True)
    slug = models.SlugField(max_length=45)


    def __unicode__(self):
        return self.surname


class Dossier(models.Model):
    COLORS = (('r', 'red'),
              ('o', 'orange'),
              ('y', 'yellow'),
              ('g', 'green'),
              ('b', 'blue'))
    address = models.ForeignKey(Address, blank=True, null=True)
    unliked_courses = models.ManyToManyField(Course, blank=True,
                                             null=True)
    favourite_color = models.CharField(max_length=1, choices=COLORS,
                                       default='r', blank=True)

    def __unicode__(self):
        return "Dossier %d" % self.id
