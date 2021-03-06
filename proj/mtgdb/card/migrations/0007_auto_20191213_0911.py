# Generated by Django 3.0 on 2019-12-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_auto_20191213_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='colors',
            field=models.CharField(choices=[('White', 'White'), ('Blue', 'Blue'), ('Black', 'Black'), ('Rred', 'Red'), ('Green', 'Green'), ('Colorless', 'Colorless'), ('Multicolored', 'Multicolored')], max_length=45),
        ),
        migrations.AlterField(
            model_name='card',
            name='rarity',
            field=models.CharField(choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare'), ('Mythic Rare', 'Mystic Rare')], max_length=45),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(choices=[('Creature', 'Creature'), ('Artifact', 'Artifact'), ('Enchantment', 'Enchantment'), ('Instant', 'Instant'), ('Sorcery', 'Sorcery'), ('Land', 'Land')], max_length=45),
        ),
    ]
