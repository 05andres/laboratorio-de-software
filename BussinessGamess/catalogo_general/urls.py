from django.urls import path
from .views import  catalogo_General ,AuthorDetail
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST


urlpatterns = [
    path('general/',catalogo_General.as_view(),name="general"),
    path('<pk>/detalles/',AuthorDetail.as_view(), name='detalles')

]