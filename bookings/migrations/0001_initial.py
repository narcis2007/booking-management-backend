# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=1)),
                ('sex', models.CharField(default=b'm', max_length=1)),
                ('cnp', models.CharField(default=b'1234', max_length=20)),
                ('date1', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'first date')),
                ('date2', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'second date')),
                ('date3', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'third date')),
                ('description', models.CharField(default=b'no description', max_length=256)),
                ('clinic', models.CharField(default=b'unknown', max_length=256)),
                ('code', models.CharField(default=b'123456', max_length=6, serialize=False, primary_key=True)),
                ('final_date', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'final date')),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date1', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'first date')),
                ('date2', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'second date')),
                ('date3', models.DateTimeField(default=b'0001-01-01T01:01:00Z', verbose_name=b'third date')),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CheckBooking',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('status', models.CharField(default=b'Wrong code, please enter a valid one', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'unknown', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(default=b'waiting', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.ForeignKey(default=1, to='bookings.Status'),
        ),
    ]
