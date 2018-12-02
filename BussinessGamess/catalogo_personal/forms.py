from django import forms
from .models import Videojuegos

class VideojuegosForm(forms.ModelForm):
    class Meta:
        model = Videojuegos
        fields = ('title','FechaLanzamiento','precio','categoria','duracionPromedio','sinopsis','image')
    
    def __init__(self, *args, **kwargs):
        super(VideojuegosForm, self).__init__(*args, **kwargs)
        self.fields['title'].label=''
        self.fields['FechaLanzamiento'].label=''
        self.fields['precio'].label=''
        self.fields['categoria'].label=''
        self.fields['duracionPromedio'].label=''
        self.fields['sinopsis'].label=''
        self.fields['image'].label=''
        self.fields['title'].widget = forms.TextInput(attrs={ 'type':"text",'class':'form-control','id':'exampleInputEmail1', 'aria-describedby':'emailHelp', 'placeholder':'Ingresar nombre de videojuego'})
        self.fields['FechaLanzamiento'].widget = forms.DateInput(attrs={ 'type':'text', 'class':'form-control' ,'id':'exampleInputEmail1','aria-describedby':'emailHelp' ,'placeholder':'Año de lanzamiento DD/MM/AAAA'})
        self.fields['precio'].widget = forms.TextInput(attrs={'type':'number','class':'form-control','id':'exampleInputEmail1','aria-describedby':'emailHelp','placeholder':'Precio'})
        self.fields['categoria'].widget = forms.TextInput(attrs={ 'type':'text', 'class':'form-control','id':'exampleInputEmail1' ,'aria-describedby':'emailHelp' ,'placeholder':'Género'})
        self.fields['duracionPromedio'].widget = forms.TextInput(attrs={ 'type':'text', 'class':'form-control','id':'exampleInputEmail1' ,'aria-describedby':'emailHelp','placeholder':'Duración (ej: 1 hora,1 dia,1 año)'})
        self.fields['sinopsis'].widget = forms.Textarea(attrs={'class':'form-control' ,'id':'exampleFormControlTextarea1','rows':'3'})
        self.fields['image'].widget = forms.ClearableFileInput(attrs={'type':'file','class':'custom-file-input','id':'customFile','style':'display:none'})