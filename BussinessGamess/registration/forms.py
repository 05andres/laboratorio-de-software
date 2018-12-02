from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label=''
        self.fields['password1'].label=''
        self.fields['password2'].label=''
        self.fields['first_name'].label=''
        self.fields['last_name'].label=''
        self.fields['email'].label=''
        self.fields['password2'].help_text=''
        self.fields['username'].help_text='Únicamente letras, digitos y @/,/+/-/_'
        self.fields['username'].widget =forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Ingresa un nombre de usuario'})
        self.fields['password1'].widget =forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Ingresa una Contraseña'})
        self.fields['password2'].widget =forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Confirma tu Contraseña'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Ingresa tu Nombre'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Ingresa tu Apellido'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control form-control-lg','placeholder':'Dirección de correo electrónico'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dni','telefono', 'FechaNacimiento')
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['dni'].label=''
        self.fields['telefono'].label=''
        self.fields['FechaNacimiento'].label=''
        self.fields['dni'].widget = forms.TextInput(attrs={'class':'form-control form-control-lg','type':'number','placeholder':'Ingresa tu Cédula'})
        self.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control form-control-lg','type':'number','placeholder':'Télefono de Contacto'})
        self.fields['FechaNacimiento'].widget = forms.DateInput(attrs={'class':'form-control form-control-lg','placeholder':'Fecha de nacimiento DD/MM/AAAA'})
