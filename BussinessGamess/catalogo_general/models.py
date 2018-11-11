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
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación",blank=True,null=True)

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        ordering = ["created"]
    
    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('Videojuegos:comentarios', kwargs={'pk': self.pk})


