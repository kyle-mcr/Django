# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-16 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release',
            field=models.DateField(),
        ),
    ]
