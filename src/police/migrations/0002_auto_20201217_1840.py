# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-12-17 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='id',
            field=models.CharField(choices=[('Bangalore', 'Bangalore'), ('Mangalore', 'Mangalore'), ('Shivamogga', 'Shivamogga'), ('Chikmangalore', 'Chikmangalore'), ('Udpi', 'Udpi'), ('Sagara', 'Sagara'), ('Siddapura', 'Siddapura'), ('Gadag', 'Gadag'), ('Bijapur', 'Bijapur'), ('Bagalkote', 'Bagalkote'), ('Rampura', 'Rampura'), ('Other', 'Other')], max_length=10, primary_key=True, serialize=False),
        ),
    ]
