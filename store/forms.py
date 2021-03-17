from django.forms import fields
from moviestore.models import Movie
from django import forms
from django.forms.widgets import TextInput


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['nomi', 'janr', 'narxi', 'yili', 'davomiyligi', 'movie', 'batafsil', 'avtor', 'rasm']