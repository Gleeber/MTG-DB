# Generated by Django 3.0 on 2019-12-13 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20191212_2154'),
        ('match', '0003_match_player_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='players.Player'),
        ),
    ]
