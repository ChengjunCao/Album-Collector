from django.shortcuts import render, redirect
from .models import Album, Cover
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TrackForm
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'albumcollector'

def albums_index(request):
  albums = Album.objects.filter(user=request.user)
  return render(request, 'albums/index.html', {'albums': albums})

def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  track_form = TrackForm()
  return render(request, 'albums/detail.html', {'album': album, 'track_form': track_form,})

class AlbumCreate(CreateView):
  model = Album
  fields = ['name', 'artists', 'genre', 'year']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# View without CBV

# def albums_index(request):
#   albums = Album.objects.all()
#   return render(request, 'albums/index.html', {'albums': albums})

# def albums_detail(request, album_id):
#   album = Album.objects.get(id=album_id)
#   track_form = TrackForm
#   return render(request, 'albums/detail.html', {'album': album,
#   'track_form': track_form})
