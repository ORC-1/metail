# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-02 12:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('metailnook', '0007_auto_20180731_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_profile',
            name='Company_name',
            field=models.CharField(default=datetime.datetime(2018, 8, 2, 12, 34, 40, 507000, tzinfo=utc), max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account_profile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='account_profile',
            name='position',
            field=models.CharField(max_length=100, verbose_name='position'),
        ),
    ]