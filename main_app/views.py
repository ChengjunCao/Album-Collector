from django.shortcuts import render

from .models import Album

# Add the Cat class & list and view function below the imports

# class Album:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, artists, genre, year):
#     self.name = name
#     self.artists = artists
#     self.genre = genre
#     self.year = year

# albums = [
#     Album('American Beauty', 'Grateful Dead', 'Folk Rock', 1970),
#     Album('\'Allelujah! Don\'t Bend! Ascend', 'Godspeed You! Black Emperor', 'Post-Rock', 2012),
#     Album('Microphones in 2020', 'The Microphones', 'Indie Folk', 2020),
#     Album('冀西南林路行', '万能青年旅店', 'Folk Rock', 2020)
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def albums_index(request):
  albums = Album.objects.all()
  return render(request, 'albums/index.html', {'albums': albums})

def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  return render(request, 'albums/detail.html', {'album': album})
