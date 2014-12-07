# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=b'python', max_length=20, choices=[(b'PY', b'python'), (b'PHP', b'php'), (b'JAVA', b'java')])),
                ('name', models.CharField(max_length=25)),
                ('data_start', models.DateField()),
                ('data_finish', models.DateField()),
                ('assistant', models.ForeignKey(related_name='assistant', to='Coaches.Coach')),
                ('teacher', models.ForeignKey(related_name='teacher', to='Coaches.Coach')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
