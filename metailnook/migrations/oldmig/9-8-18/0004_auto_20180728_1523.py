# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metailnook', '0003_navbar_link_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blouse',
            old_name='Halflength',
            new_name='halflength',
        ),
        migrations.RenameField(
            model_name='gown',
            old_name='Halflength',
            new_name='halflength',
        ),
        migrations.AlterField(
            model_name='payment',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
