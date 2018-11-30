from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('text',)

class SearchForm(forms.Form):
    nombre = forms.CharField(max_length=100,required=False)
