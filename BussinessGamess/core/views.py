from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get(self,request,*args,**kwaegs):
        return render(request,self.template_name,{'title': "BussinessGames"})

class BasePageView(TemplateView):
    template_name = "core/base.html"
    
    def get(self,request,*args,**kwaegs):
        return render(request,self.template_name,{'title': "BussinessGames"})


class BienvenidaPageView(TemplateView):
    template_name = "core/bienvenida.html"

    @method_decorator(login_required)
    def get(self,request,*args,**kwaegs):
        return render(request,self.template_name,{'title': "Bienvenida"})