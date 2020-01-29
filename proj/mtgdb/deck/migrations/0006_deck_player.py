# Generated by Django 3.0 on 2019-12-12 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20191212_2154'),
        ('deck', '0005_auto_20191212_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.Player'),
        ),
    ]