from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Match(models.Model):
    player_one = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='player_one', null=True)
    player_two = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='player_two', null=True)
    winner = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='winner', blank=True, null=True, editable=False)
    loser = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='loser', blank=True, null=True, editable=False)
    player_one_wins = models.IntegerField(blank=True, null=True)
    player_two_wins = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.player_one.fname + " vs. " + self.player_two.fname

def update_match_winner(sender, **kwargs):
    match = kwargs['instance']
    if match.player_one_wins is not None and match.player_two_wins is not None and match.winner is None and match.loser is None:
        if match.player_one_wins > match.player_two_wins:
            match.winner = match.player_one
            match.loser = match.player_two
        elif match.player_one_wins < match.player_two_wins:
            match.winner = match.player_two
            match.loser = match.player_one
        match.save()
    if match.winner is not None:
        if match.winner == match.player_one:
            if match.player_one_wins < match.player_two_wins:
                match.winner = match.player_two
                match.loser = match.player_one
                match.save()
        if match.winner == match.player_two:
            if match.player_one_wins > match.player_two_wins:
                match.winner = match.player_one
                match.loser = match.player_two
                match.save()

post_save.connect(update_match_winner, sender=Match)
