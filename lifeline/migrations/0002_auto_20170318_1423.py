# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 03:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
