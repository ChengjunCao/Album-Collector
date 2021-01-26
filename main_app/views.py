from django.shortcuts import render, redirect
from .models import Album
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TrackForm

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
  track_form = TrackForm
  return render(request, 'albums/detail.html', {'album': album, 
  'track_form': track_form})

def add_track(request, album_id):
  form = TrackForm(request.POST)
  if form.is_valid():
    new_track = form.save(commit=False)
    new_track.album_id = album_id
    new_track.save()
  return redirect('detail', album_id=album_id)