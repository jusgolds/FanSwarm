# Generated by Django 2.0.1 on 2018-03-07 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0014_favoriteteam_fav_team_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteteam',
            name='fav_team',
        ),
        migrations.RemoveField(
            model_name='favoriteteam',
            name='fav_team_league',
        ),
        migrations.RemoveField(
            model_name='favoriteteam',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorite_teams',
        ),
        migrations.DeleteModel(
            name='FavoriteTeam',
        ),
    ]