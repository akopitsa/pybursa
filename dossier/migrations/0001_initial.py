# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_auto_20141207_1422'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=25, choices=[(b'RED', b'red'), (b'WHITE', b'white'), (b'BLACK', b'black'), (b'YELLOW', b'yellow'), (b'GREEN', b'green'), (b'BLUE', b'blue'), (b'GREY', b'grey')])),
                ('addr', models.ForeignKey(related_name='dossier_of', to='address.Address')),
                ('unlikecourse', models.ManyToManyField(related_name='dossier_of', to='Course.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
