# Generated by Django 2.0.1 on 2018-02-28 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0013_auto_20180225_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteteam',
            name='fav_team_league',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fs.League'),
            preserve_default=False,
        ),
    ]
