# Generated by Django 2.0.1 on 2018-02-20 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0004_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='fs.FanGroup'),
        ),
    ]