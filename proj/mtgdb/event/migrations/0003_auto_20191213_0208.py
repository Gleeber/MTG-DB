# Generated by Django 3.0 on 2019-12-13 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0001_initial'),
        ('event', '0002_event_game_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game_store',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='game_store.GameStore'),
        ),
    ]
