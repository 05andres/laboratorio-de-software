from django.urls import path
from .views import VideojuegosViews, catalogo,detalles_videojuegos_personal,descontando
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('videojuegos/', login_required(VideojuegosViews.as_view()),name="videojuego"),
    path('catalogo/',login_required(views.catalogo),name="catalogo"),
    path('<pk>/detallespersonal/', login_required(detalles_videojuegos_personal.as_view()),name="detallespersonal"),
    path('descuentos/',views.descontando,name='descuentos'),

]