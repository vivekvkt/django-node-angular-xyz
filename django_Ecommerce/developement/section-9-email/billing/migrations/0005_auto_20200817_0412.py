# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-08-17 04:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='last_4',
            new_name='card_last4_digit',
        ),
    ]
