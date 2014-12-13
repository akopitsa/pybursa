# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=65)),
                ('phone', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=15, choices=[(b'TEACHER', b'teacher'), (b'ASSISTANT', b'assistant')])),
            ],
            options={
                'verbose_name': '\u0422\u0420\u0415\u041d\u0415\u0420\u0410',
            },
            bases=(models.Model,),
        ),
    ]
