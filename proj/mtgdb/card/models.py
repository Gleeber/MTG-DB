from django.db import models
from django.apps import apps

# Create your models here.
class Card(models.Model):
    TYPE_CHOICES = [
        ('Creature','Creature'),
        ('Planeswalker', 'Planeswalker'),
        ('Artifact','Artifact'),
        ('Enchantment','Enchantment'),
        ('Instant','Instant'),
        ('Sorcery','Sorcery'),
        ('Land','Land'),
    ]

    COLOR_CHOICES = [
        ('White', 'White'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('Rred', 'Red'),
        ('Green', 'Green'),
        ('Colorless', 'Colorless'),
        ('Multicolored', 'Multicolored'),
    ]

    RARITY_CHOICES = [
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Mythic Rare', 'Mythic Rare'),
    ]
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45, choices=TYPE_CHOICES)
    cmc = models.IntegerField()
    colors = models.CharField(max_length=45, choices=COLOR_CHOICES)
    set = models.CharField(max_length=45)
    rarity = models.CharField(max_length=45, choices=RARITY_CHOICES)

    def __str__(self):
        return self.name