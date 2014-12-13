# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('technology', models.CharField(max_length=15, choices=[(b'PYTHON', b'python'), (b'PHP', b'php'), (b'JAVA', b'java')])),
                ('assist', models.ForeignKey(related_name='assist', to='coach.Coach')),
                ('teacher', models.ForeignKey(related_name='teacher', to='coach.Coach')),
                ('venue', models.ForeignKey(to='address.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
