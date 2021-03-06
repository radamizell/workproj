# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 21:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnum', models.IntegerField(null=True)),
                ('blocked', models.BooleanField(default=False)),
                ('sun_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('sun_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('mon_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('mon_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('tue_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('tue_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('wed_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('wed_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('thu_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('thu_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('fri_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('fri_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('sat_begin_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('sat_end_time', models.TimeField(blank=True, choices=[(datetime.time(0, 0), '12 AM'), (datetime.time(1, 0), '1 AM'), (datetime.time(2, 0), '2 AM'), (datetime.time(3, 0), '3 AM'), (datetime.time(4, 0), '4 AM'), (datetime.time(5, 0), '5 AM'), (datetime.time(6, 0), '6 AM'), (datetime.time(7, 0), '7 AM'), (datetime.time(8, 0), '8 AM'), (datetime.time(9, 0), '9 AM'), (datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM')], null=True)),
                ('sun', models.BooleanField(default=False)),
                ('mon', models.BooleanField(default=False)),
                ('tue', models.BooleanField(default=False)),
                ('wed', models.BooleanField(default=False)),
                ('thu', models.BooleanField(default=False)),
                ('fri', models.BooleanField(default=False)),
                ('sat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NumObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('ident', models.IntegerField()),
                ('usersave', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sound', models.FileField(upload_to=b'')),
                ('numobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.BlackList')),
            ],
        ),
        migrations.AddField(
            model_name='blacklist',
            name='numkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.NumObject'),
        ),
    ]
