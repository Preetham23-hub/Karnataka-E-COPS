# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-12-17 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_case_ward_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='witness',
            name='bahmashah_id',
        ),
    ]
