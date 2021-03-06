# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[('M', 'M\xe4nnlich'), ('W', 'Weiblich')], max_length=1)),
                ('birthday', models.DateField()),
                ('juleica_date', models.DateField()),
                ('first_aid_date', models.DateField()),
                ('einsegnung_date', models.DateField()),
                ('nc_year', models.PositiveSmallIntegerField()),
                ('landline', models.CharField(max_length=15)),
                ('mobilephone', models.CharField(max_length=20)),
                ('facebook_link', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='pictures/')),
                ('picture_date', models.DateField()),
                ('street', models.CharField(max_length=30)),
                ('street_no', models.PositiveSmallIntegerField()),
                ('zipcode', models.PositiveSmallIntegerField()),
                ('city', models.CharField(max_length=30)),
                ('addition', models.CharField(max_length=100)),
                ('first_commway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Commways')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Group')),
            ],
        ),
    ]
