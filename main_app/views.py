from django.shortcuts import render, redirect
from .models import Album, Cover
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TrackForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'albumcollector'

class AlbumList(ListView):
  model = Album
  template_name = 'albums/index.html'

class AlbumDetail(DetailView):
  model = Album
  template_name = 'albums/detail.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['track_form'] = TrackForm()
      return context

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

def add_track(request, album_id):
  form = TrackForm(request.POST)
  if form.is_valid():
    new_track = form.save(commit=False)
    new_track.album_id = album_id
    new_track.save()
  return redirect('detail', pk=album_id)

def add_cover(request, album_id):
  # cover-file will be the "name" attribute on the <input type="file">
  cover_file = request.FILES.get('cover-file', None)
  if cover_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + cover_file.name[cover_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(cover_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to album_id or album (if you have an album object)
      cover = Cover(url=url, album_id=album_id)
      cover.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', pk=album_id)

# View without CBV

# def albums_index(request):
#   albums = Album.objects.all()
#   return render(request, 'albums/index.html', {'albums': albums})

# def albums_detail(request, album_id):
#   album = Album.objects.get(id=album_id)
#   track_form = TrackForm
#   return render(request, 'albums/detail.html', {'album': album,
#   'track_form': track_form})
