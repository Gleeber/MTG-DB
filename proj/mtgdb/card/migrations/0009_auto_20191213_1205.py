# Generated by Django 3.0 on 2019-12-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_auto_20191213_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(choices=[('Creature', 'Creature'), ('Planeswalker', 'Planeswalker'), ('Artifact', 'Artifact'), ('Enchantment', 'Enchantment'), ('Instant', 'Instant'), ('Sorcery', 'Sorcery'), ('Land', 'Land')], max_length=45),
        ),
    ]