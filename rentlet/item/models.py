from django.db import models

# Create your models here.
from rentlet_user.models import RentletUser


class Item(models.Model):
    item_name = models.CharField(max_length=200, default="name")
    photo_link = models.CharField(max_length=200, blank=True, null=True)
    item_desc = models.TextField(max_length=200, default="", blank=True, null=True)
    created_by = models.ForeignKey(RentletUser, related_name="creator")

    def __unicode__(self):
        return self.item_name

    def to_string(self):
        return {
            'name': self.item_name,
            'photo_link': self.photo_link,
            'created_by': self.created_by_id
        }
