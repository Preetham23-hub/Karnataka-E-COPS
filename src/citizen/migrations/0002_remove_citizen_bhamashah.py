# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-09 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='bhamashah',
        ),
    ]