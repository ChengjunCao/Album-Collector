from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.CharField(max_length=100)
    genre = models.TextField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return self.name