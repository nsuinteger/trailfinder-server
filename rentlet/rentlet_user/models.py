from django.db import models

# Create your models here.

class RentletUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=10)

    def __unicode__(self):
        return self.username

