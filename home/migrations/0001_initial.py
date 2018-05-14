# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation_text', models.CharField(max_length=500)),
                ('parameters', models.CharField(max_length=500)),
                ('variables', models.CharField(max_length=200)),
                ('x_min', models.FloatField()),
                ('x_max', models.FloatField()),
                ('number_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('number', models.FloatField()),
            ],
        ),
    ]
