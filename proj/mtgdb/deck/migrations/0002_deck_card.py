# Generated by Django 3.0 on 2019-12-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='card',
            field=models.ManyToManyField(to='card.Card'),
        ),
    ]
