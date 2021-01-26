from django.shortcuts import render
from .models import Album
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class AlbumList(ListView):
  model = Album
  template_name = 'albums/index.html'

class AlbumCreate(CreateView):
  model = Album
  fields = '__all__'
  success_url = '/albums/'

class AlbumUpdate(UpdateView):
  model = Album
  fields = ['artists', 'genre', 'year']

class AlbumDelete(DeleteView):
  model = Album
  success_url = '/albums/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def albums_index(request):
#   albums = Album.objects.all()
#   return render(request, 'albums/index.html', {'albums': albums})

def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  return render(request, 'albums/detail.html', {'album': album})
