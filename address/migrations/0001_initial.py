# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.CharField(max_length=35)),
                ('country', models.CharField(max_length=55)),
                ('oblast', models.CharField(max_length=75)),
                ('district', models.CharField(max_length=75)),
                ('street', models.CharField(max_length=75)),
                ('house', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
