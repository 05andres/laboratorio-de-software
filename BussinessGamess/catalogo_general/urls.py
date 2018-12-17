from django.urls import path
from .views import  catalogo_General ,detalles_videojuegos,comentarBDD,lista_comentarios,votacion,busqueda,catalogo_busqueda,venta
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST

'''path('lista_comentarios/',views.lista_comentarios,name="lista_comentarios"),'''
urlpatterns = [
    path('general/',catalogo_General.as_view(),name="general"),                                                                                                                                                                    
    path('<pk>/detalles/',detalles_videojuegos.as_view(), name='detalles'),
    path('comentarBDD/',views.comentarBDD,name="comentarBDD"),
    path('lista_comentarios/',views.lista_comentarios,name="lista_comentarios"),
    path('votacion/',views.Votacion,name="votacion"),
    path('buscador/',views.busqueda,name='buscador'),
    path('busqueda/',catalogo_busqueda.as_view(),name="busqueda"),
    path('venta/',views.venta,name="venta"),                                                                                                                                                                    
                                                                                                                                                                 

       

]