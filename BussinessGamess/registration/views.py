
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from .forms import ProfileForm,UserForm
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login



class SignUpView(View):
    def get(self, request):
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request, 'registration/signup.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    @transaction.atomic
    def post(self,request):
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = ProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                new_user = user_form.save()
                profile = profile_form.save(commit=False)
                if profile.user_id is None:
                    profile.user_id = new_user.id    
                user_form.save()
                profile_form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect(reverse_lazy('core:bienvenida') +'?register')
        
            return render(request, 'registration/signup.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

        
                
        