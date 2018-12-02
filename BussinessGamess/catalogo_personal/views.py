from django.shortcuts import render
from django.views.generic import View
from .forms import VideojuegosForm
from django.db import transaction
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Videojuegos


class VideojuegosViews(View):
    def get(self, request):
        videojuegos_form = VideojuegosForm()
        return render(request, 'catalogo_personal/videojuego.html', {
            'videojuegos_form':videojuegos_form,
        })

    @transaction.atomic
    def post(self,request):
        if request.method == 'POST':
            print("hola")
            videojuegos_form= VideojuegosForm(request.POST,request.FILES)
            print(videojuegos_form.errors)
            if videojuegos_form.is_valid():
                print("hola if")
                new_videojuego =videojuegos_form.save(commit=False)
                new_videojuego.owner = request.user
                new_videojuego.save()
                return redirect(reverse_lazy('catalogo') +'?register')
        
            return render(request, 'catalogo_personal/videojuego.html', {
            'videojuegos_form':videojuegos_form,
        })
        
def catalogo(request):
    catalogo = Videojuegos.objects.filter(owner_id=request.user.id)
    print (request.user)
    return render(request,"catalogo_personal/catalogo.html",{'catalogo':catalogo,'title': "Catalogo personal"})
