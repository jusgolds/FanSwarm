# Generated by Django 2.0.1 on 2018-02-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0022_teams_fan_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_fan',
            name='password_hash',
            field=models.CharField(default=None, max_length=128),
        ),
    ]