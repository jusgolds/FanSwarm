# Generated by Django 2.0.1 on 2018-02-16 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0034_favorite_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fav_epl',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_mlb',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_mls',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_nba',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_ncaabb',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_ncaafb',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_nfl',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fav_nhl',
        ),
    ]