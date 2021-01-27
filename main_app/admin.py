from django.contrib import admin

from .models import Album, Track, Cover

admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Cover)