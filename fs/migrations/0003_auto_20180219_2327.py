# Generated by Django 2.0.1 on 2018-02-19 23:27

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0002_auto_20180219_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128),
        ),
    ]
