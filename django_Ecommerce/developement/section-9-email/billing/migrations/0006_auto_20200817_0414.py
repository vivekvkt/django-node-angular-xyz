# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-08-17 04:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_auto_20200817_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_last4_digit',
            new_name='last_4',
        ),
    ]
