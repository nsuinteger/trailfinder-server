from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    photo_link = models.CharField(max_length=200)