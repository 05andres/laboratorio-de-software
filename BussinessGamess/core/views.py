from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from catalogo_personal.models import Videojuegos
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Avg

# Create your views here.
#vista del home
class HomePageView(ListView):
    template_name = "core/home.html"
    model = Videojuegos
    context_object_name = 'videojuegos'
    def get_queryset(self):
        return Videojuegos.objects.only('title','image','categoria','id').annotate(Avg('votacion__valor_votacion')).filter(votacion__valor_votacion__avg__range=(4,5))

class BasePageView(TemplateView):
    template_name = "core/base.html"
    
    def get(self,request,*args,**kwaegs):
        return render(request,self.template_name,{'title': "BusinessGames"})

#vista de bienvenida cuando el usuario se registea con exito
class BienvenidaPageView(TemplateView):
    template_name = "core/bienvenida.html"

    @method_decorator(login_required)
    def get(self,request,*args,**kwaegs):
        return render(request,self.template_name,{'title': "Bienvenida"})