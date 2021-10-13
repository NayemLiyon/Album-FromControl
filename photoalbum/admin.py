from django.contrib import admin
from .models import Album

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title','short_disc','image']
    search_fields = ['title']

admin.site.register(Album,AlbumAdmin)