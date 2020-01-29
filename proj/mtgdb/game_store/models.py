from django.db import models

# Create your models here.
class GameStore(models.Model):
    name = models.CharField(max_length=255)
    phone_num = models.IntegerField()
    street = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zip = models.IntegerField()

    def __str__(self):
        return self.name

    def phone_num_formatted(self):
        phone_num = str(self.phone_num)
        return phone_num[0:3] + "-" + phone_num[3:6] + "-" + phone_num[6:10]

    def address(self):
        return self.street + ", " + self.city + ", " + self.state + ", " + str(self.zip)