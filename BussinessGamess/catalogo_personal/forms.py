from django import forms
from .models import Videojuegos

class VideojuegosForm(forms.ModelForm):
    class Meta:
        model = Videojuegos
        fields = ('title','FechaLanzamiento','categoria','duracionPromedio','sinopsis','image')
