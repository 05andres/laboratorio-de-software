from django.urls import path
from .views import HomePageView ,BasePageView,BienvenidaPageView
from django.contrib.auth.decorators import login_required, permission_required

#manejo urls de cada vista
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('', BasePageView.as_view(), name="base"),
    path('bienvenida/', login_required(BienvenidaPageView.as_view()),name="bienvenida"), 
]