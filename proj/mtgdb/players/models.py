from django.db import models

# Create your models here.
class Player(models.Model):
    dci_num = models.IntegerField()
    fname = models.CharField(max_length=45)
    mi = models.CharField(max_length=1, blank=True)
    lname = models.CharField(max_length=45)

    def __str__(self):
        returnStr = self.fname + " "
        if self.mi:
            returnStr += self.mi + ". "
        returnStr += self.lname
        return returnStr

    def name(self):
        returnStr = self.fname + " "
        if self.mi:
            returnStr += self.mi + ". "
        returnStr += self.lname
        return returnStr