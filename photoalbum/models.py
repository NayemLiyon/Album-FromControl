from django.db import models
from django.shortcuts import render

#my
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    short_disc = models.TextField()
    image = models.ImageField(upload_to='albumphotos/')
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_delete_url(self):
        return reverse('photoalbum:delete',kwargs={
            'id' : self.id
        })

    def get_update_url(self):
        return reverse('photoalbum:update',kwargs={
            'id':self.id
        })