# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-21 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_libros_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
