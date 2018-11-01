from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#vista del home
class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get(self,request,*args,**kwaegs):
        return render(request,self.template_name,{'title': "BusinessGames"})
#vista base del proyecto se vera en cada cambio de template
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