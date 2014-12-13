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
                ('postindex', models.CharField(max_length=7)),
                ('country', models.CharField(max_length=55)),
                ('obl', models.CharField(max_length=55)),
                ('district', models.CharField(max_length=55)),
                ('street', models.CharField(max_length=55)),
                ('house', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
