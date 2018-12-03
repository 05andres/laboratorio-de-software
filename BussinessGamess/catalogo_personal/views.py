from django.shortcuts import render
from django.views.generic import View
from .forms import VideojuegosForm
from django.db import transaction
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Videojuegos
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Avg
from django.http import JsonResponse




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
                new_videojuego.Descuento = 0
                new_videojuego.save()
                return redirect(reverse_lazy('catalogo') +'?register')
        
            return render(request, 'catalogo_personal/videojuego.html', {
            'videojuegos_form':videojuegos_form,
        })
        
def catalogo(request):
    catalogo = Videojuegos.objects.filter(owner_id=request.user.id)
    print (request.user)
    return render(request,"catalogo_personal/catalogo.html",{'catalogo':catalogo,'title': "Catalogo personal"})

class detalles_videojuegos_personal(DetailView):
    template_name = 'catalogo_personal/detallespersonal.html'
    model = Videojuegos
    context_object_name = 'videojuego'

def descontando(request):
    data={}
    if request.is_ajax():
        videojuego=request.POST['videojuego']
        precio=request.POST['precio']
        descontar=request.POST['descuento']
        porcentaje=(int(descontar)/100)*int(precio)
        valor_entero=int(precio)-porcentaje
        p = Videojuegos.objects.get(id=videojuego)
        print(int(valor_entero))
        p.Descuento=int(valor_entero)
        p.save()
        data['mensaje']="Descuento Asignado"
        return JsonResponse(data,safe=False)


    
