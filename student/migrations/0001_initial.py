# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favourite_color', models.CharField(default=b'r', max_length=1, blank=True, choices=[(b'r', b'red'), (b'o', b'orange'), (b'y', b'yellow'), (b'g', b'green'), (b'b', b'blue')])),
                ('address', models.ForeignKey(blank=True, to='address.Address', null=True)),
                ('unliked_courses', models.ManyToManyField(to='course.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('surname', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=76)),
                ('phone', models.CharField(max_length=17)),
                ('package', models.CharField(max_length=8, choices=[(b'STANDART', b'standart'), (b'VIP', b'vip'), (b'GOLD', b'gold')])),
                ('dossier', models.OneToOneField(null=True, blank=True, to='student.Dossier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
