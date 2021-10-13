from django import forms
from django.shortcuts import render

#my
from photoalbum.forms import AddForms
from .models import Album
from django.views.generic import CreateView,DeleteView,UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Album_Create(LoginRequiredMixin,CreateView):
    model = Album
    form_class = AddForms
    template_name = 'album/create.html'
    success_url = '/'


class DeleteAlbum(DeleteView):
    template_name = 'album/delete.html'


    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Album,id=id)

    def get_success_url(self):
        return reverse('photoalbum:index')


class UpdateAlbum(UpdateView):
    template_name = 'album/update.html'
    form_class = AddForms


    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Album,id=id)

    def get_success_url(self):
        return reverse('photoalbum:index')


def albumfunc(request):
    album_data  = Album.objects.all()
    contex={

        'album_data' : album_data
    }
    return render(request,'album/index.html',contex)