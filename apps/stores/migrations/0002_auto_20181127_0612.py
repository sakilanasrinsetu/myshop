# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openingperiod',
            name='weekday',
            field=models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Public Holidays')], verbose_name='Weekday'),
        ),
    ]
