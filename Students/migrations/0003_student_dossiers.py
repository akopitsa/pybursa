# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0001_initial'),
        ('Students', '0002_auto_20141210_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dossiers',
            field=models.OneToOneField(related_name='student_of', default=1, to='dossier.Dossier'),
            preserve_default=False,
        ),
    ]
