# Generated by Django 4.1.5 on 2023-01-19 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='subsciptionDurationInMonths',
            new_name='subsciptionExpireInMonths',
        ),
    ]
