from django.db import models

# Create your models here.
class Deck(models.Model):
    FORMAT_CHOICES = [
        ('Standard', 'Standard'),
        ('Commander', 'Commander'),
        ('Modern', 'Modern'),
        ('Legacy', 'Legacy'),
        ('Vintage', 'Vintage'),
        ('Brawl', 'Brawl')
    ]

    name = models.CharField(max_length=45)
    card = models.ManyToManyField('card.Card', through='Membership')
    player = models.ForeignKey('players.Player', models.SET_NULL, blank=True, null=True)
    format = models.CharField(max_length=45, choices=FORMAT_CHOICES)

    def __str__(self):
        return self.name

class Membership(models.Model):
    card = models.ForeignKey('card.Card', on_delete=models.SET_NULL, null=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    qty = models.IntegerField()
