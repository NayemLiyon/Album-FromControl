from django import forms
from django.db.models import fields
from .models import Album

class AddForms(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title','short_disc','image')
