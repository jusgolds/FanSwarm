# Generated by Django 2.0.1 on 2018-02-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0036_auto_20180216_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmed',
            field=models.BooleanField(default=0),
        ),
    ]
