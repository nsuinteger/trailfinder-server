from django.conf import settings
from django.db import models

# Create your models here.


class RentletUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return self.user.username

