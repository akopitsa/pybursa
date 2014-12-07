# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20141207_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=25, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
    ]
