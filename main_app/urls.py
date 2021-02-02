from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('albums/', views.albums_index, name='index'),
  path('albums/<int:album_id>/', views.albums_detail, name='detail'),
  path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
  path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
  path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete'),
  path('albums/<int:album_id>/add_track/', views.add_track, name='add_track'),
  path('albums/<int:album_id>/add_cover/', views.add_cover, name='add_cover'),
  path('accounts/signup/', views.signup, name='signup'),
]
