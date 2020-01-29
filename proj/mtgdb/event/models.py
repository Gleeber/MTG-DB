from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateTimeField()
    format = models.CharField(max_length=45)
    game_store = models.ForeignKey('game_store.GameStore',on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.name