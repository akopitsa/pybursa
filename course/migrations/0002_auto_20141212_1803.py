# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='technology',
            field=models.CharField(max_length=15, choices=[(b'PYTHON', b'python'), (b'PHP', b'php'), (b'JAVA', b'java'), (b'C#', b'c#')]),
            preserve_default=True,
        ),
    ]
