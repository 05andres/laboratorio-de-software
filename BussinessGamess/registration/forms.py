from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dni','telefono', 'FechaNacimiento')
