# Generated by Django 2.2 on 2020-10-27 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudeappangular', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
