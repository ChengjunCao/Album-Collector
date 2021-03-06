from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

DISC = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
)

class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})

class Track(models.Model):
    disc = models.IntegerField(
        choices=DISC,
        default=DISC[0]
    )
    number = models.IntegerField()
    title= models.CharField(max_length=100)
    length = models.CharField(max_length=100)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['number']

class Cover(models.Model):
    url = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cover for album_id: {self.album_id} @{self.url}"
