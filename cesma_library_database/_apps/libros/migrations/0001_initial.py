# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-11 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
                ('editorial', models.CharField(max_length=60)),
                ('autor', models.CharField(max_length=90)),
                ('ISBN', models.CharField(max_length=20)),
            ],
        ),
    ]
