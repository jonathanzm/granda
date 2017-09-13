# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-08-14 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('cedula_identidad', models.CharField(max_length=13)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=14)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=30)),
                ('medidas', models.CharField(max_length=30)),
                ('tipo_producto', models.CharField(max_length=30)),
            ],
        ),
    ]
