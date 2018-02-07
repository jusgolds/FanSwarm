# Generated by Django 2.0.1 on 2018-02-07 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leagues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=120)),
                ('abbreviation', models.CharField(max_length=32)),
                ('sport', models.CharField(choices=[('BB', 'Basketball'), ('FB', 'Football'), ('BS', 'Baseball'), ('HY', 'Hockey'), ('SC', 'Soccer')], default=None, max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='teams',
            name='team_league',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fs.Leagues'),
        ),
    ]
