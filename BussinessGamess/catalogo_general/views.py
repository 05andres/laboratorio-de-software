from django.shortcuts import render
from django.views.generic import View
from django.db import transaction
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from catalogo_personal.models import Videojuegos
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin
from .forms import ComentariosForm,SearchForm
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from .models import Comentarios,votacion
from catalogo_personal.models import Videojuegos
from django.core.serializers import serialize
from django.db.models import F,Q
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your views here.
class catalogo_General(ListView):
    template_name = 'catalogo_general/general.html'
    model = Videojuegos
    context_object_name = 'catalogo_General'
    form_class = SearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Videojuegos.objects.filter(title__icontains=form.cleaned_data['nombre'])
        return Videojuegos.objects.all()

class detalles_videojuegos(DetailView):
    template_name = 'catalogo_general/detalles.html'
    model = Videojuegos
    context_object_name = 'videojuego'

def lista_comentarios(request):
    if request.method == 'GET':
        co_id = request.GET['co_id']
        comentarios = Comentarios.objects.filter(videojuego=co_id).select_related('owner')
        print (comentarios)
        data=serialize('json',comentarios)
        print(data)
        '''
        import json
        jsonToPython = json.loads(data)
        print(jsonToPython[0]['fields']['owner'])
        print (len(jsonToPython))
        lis_dueños=[]
        for i in range(0,len(jsonToPython)):
            dueños = jsonToPython[i]['fields']['owner']
            lis_dueños.append(dueños)
        print(lis_dueños)   
        owner_comment=User.objects.filter(id__in=lis_dueños).only('username')'''           
        return JsonResponse(data,safe=False) # Sending an success response

def comentarBDD(request): 
    data={}    
    if request.method == 'POST' :
            print ("hola mundo")
            comentario=request.POST['comentario']
            videojuego=Videojuegos.objects.get(id = request.POST['videojuego'])
            owner = request.user
            nombre_owner= request.user.username
            print (videojuego)
            comment=Comentarios(owner=owner,videojuego=videojuego,text=comentario,owner_username=nombre_owner)
            comment.save()
            data['nombre']= nombre_owner
            data['text']= comentario
            return JsonResponse(data,safe=False)
    
    return JsonResponse(data,safe=False)
    

def Votacion(request):
    if request.method == "POST":
        voto=request.POST['voto']
        Video=request.POST['videojuego']
        print(voto,Video)
        videogame=Videojuegos.objects.get(id = request.POST['videojuego'])
        votado=votacion.objects.create(videojuego=videogame,valor_votacion=voto)
        '''p = Videojuegos.objects.get(id=videogame) 
        stars_average = p.rating_set.aggregate(Avg('valor_votacion')).values()[0]'''
        p=Videojuegos.objects.aggregate(average_price=Avg('votacion__valor_votacion'))
        print (p)
        return JsonResponse(p,safe=False)











