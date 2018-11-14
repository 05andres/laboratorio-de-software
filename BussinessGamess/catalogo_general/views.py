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







# Create your views here.
'''def catalogo_General(request):
    catalogo_General = Videojuegos.objects.all()
    return render(request,"catalogo_general/general.html",{'catalogo_General':catalogo_General})'''
class catalogo_General(ListView):
    template_name = 'catalogo_general/general.html'
    model = Videojuegos
    context_object_name = 'catalogo_General'

class detalles_videojuegos(DetailView):
    template_name = 'catalogo_general/detalles.html'
    model = Videojuegos
    context_object_name = 'videojuego'


class AuthorDetail(FormMixin, DetailView):
    template_name = 'catalogo_general/detalles.html'
    model = Videojuegos
    form_class = ComentariosForm
    context_object_name = 'videojuego'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('detalles', kwargs={'pk': Videojuegos.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request,pk, *args, **kwargs):
        form = self.get_form()
        id_videojuego = get_object_or_404(Videojuegos, pk=pk) 
        if request.method == "POST":
            if form.is_valid():
                if request.user.is_authenticated:
                    print (id_videojuego)
                    comment = form.save(commit=False)
                    comment.owner = request.user
                    comment.videojuego =id_videojuego
                    comment.save()
                    return JsonResponse({
                        'content':{
                            'mensaje':'su mensaje ha sido recibido',
                        }

                        }
                    )
                
                else:
                     return JsonResponse({
                        'content':{
                            'mensaje':'su mensaje ha sido recibido',
                        }

                        }
                    )
 
            else:
                return render(request, 'catalogo_general/detalles.html',{'form': form})
            
            return render(request, 'catalogo_general/detalles.html',{'form':form})

    
def ComentariosViews(request, pk):
    post = get_object_or_404(Videojuegos, pk=pk)
    comentario_form = ComentariosForm(request.POST)
    if request.method == "POST":
        if comentario_form.is_valid():
            comment = comentario_form.save(commit=False)
            comment.owner = request.user
            comment.videojuego = post
            comment.save()
            return redirect('detalles', pk=post.pk)
    else:
        comentario_form = ComentariosForm()
    return render(request, 'catalogo_general/detalles.html',{'form': comentario_form})

