# Generated by Django 2.0.1 on 2018-02-11 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0019_user_fan_fav_mlb'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_fan',
            name='fav_epl',
            field=models.ForeignKey(default=None, limit_choices_to={'team_league': 5}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fs.Teams'),
        ),
        migrations.AddField(
            model_name='user_fan',
            name='fav_mls',
            field=models.ForeignKey(default=None, limit_choices_to={'team_league': 6}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fs.Teams'),
        ),
        migrations.AddField(
            model_name='user_fan',
            name='fav_nfl',
            field=models.ForeignKey(default=None, limit_choices_to={'team_league': 3}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fs.Teams'),
        ),
        migrations.AddField(
            model_name='user_fan',
            name='fav_nhl',
            field=models.ForeignKey(default=None, limit_choices_to={'team_league': 4}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fs.Teams'),
        ),
    ]