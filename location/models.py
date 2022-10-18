from asyncio.windows_events import NULL
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    categoryid = models.IntegerField
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Location(models.Model):
    locationid = models.IntegerField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    weburl= models.CharField(max_length=250)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def getCategoryId(self):
        return self.categoryid

