# Generated by Django 2.0.1 on 2018-02-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0032_auto_20180216_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sports',
            name='sport_name',
            field=models.CharField(default=None, max_length=32),
        ),
    ]