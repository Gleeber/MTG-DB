# Generated by Django 3.0 on 2019-12-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='mi',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
