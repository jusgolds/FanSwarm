# Generated by Django 2.0.1 on 2018-02-20 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0009_remove_team_fan_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='group',
        ),
    ]