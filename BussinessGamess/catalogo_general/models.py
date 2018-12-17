from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from catalogo_personal.models import Videojuegos
# Create your models here.

class Comentarios (models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    videojuego = models.ForeignKey('catalogo_personal.Videojuegos',on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación",blank=True,null=True)
    owner_username= models.CharField(max_length = 200,blank=True, null=True)

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        ordering = ["created"]
    
    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('Videojuegos:comentarios', kwargs={'pk': self.pk})

class votacion(models.Model):
    videojuego = models.ForeignKey('catalogo_personal.Videojuegos',on_delete=models.CASCADE)
    valor_votacion = models.IntegerField()
    
    class Meta:
        verbose_name="votacion"
        verbose_name_plural="votaciones"
    
    def get_absolute_url(self):
        return reverse('Videojuegos:votaciones', kwargs={'pk': self.pk})


class NotificacionesVentas(models.Model):
    user1 = models.TextField()
    user2 = models.TextField()
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación",blank=True,null=True)
    estado= models.IntegerField(null=True)#1 aceptado 0 negado
    videojuego= models.TextField() #1 venta 0 trueque
    class Meta:
        verbose_name = "notificacion"
        verbose_name_plural = "notificaciones"
        ordering = ["created"]


