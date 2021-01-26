from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})
