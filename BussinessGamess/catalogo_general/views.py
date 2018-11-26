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
from .forms import ComentariosForm
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from .models import Comentarios
from catalogo_personal.models import Videojuegos
from django.core.serializers import serialize
from django.db.models import F,Q
from django.contrib.auth.models import User
# Create your views here.
class catalogo_General(ListView):
    print("general")
    template_name = 'catalogo_general/general.html'
    model = Videojuegos
    context_object_name = 'catalogo_General'

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
            print (nombre_owner)
            comment=Comentarios(owner=owner,videojuego=videojuego,text=comentario,owner_username=nombre_owner)
            comment.save()
            data['nombre']= nombre_owner
            data['text']= comentario
            return JsonResponse(data,safe=False)
    return JsonResponse(data,safe=False)
    







