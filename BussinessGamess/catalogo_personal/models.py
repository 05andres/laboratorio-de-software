from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Videojuegos(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200,verbose_name="Titulo")
    sinopsis = models.TextField(default='',verbose_name="Ingrese una breve sinopsis del Videojuego")
    categoria = models.CharField(max_length = 200,verbose_name="Categoria")
    FechaLanzamiento= models.DateField( verbose_name="Año de lanzamiento")
    image = models.ImageField(verbose_name="Imagen", upload_to ="image_juegos")
    duracionPromedio = models.CharField(max_length = 200,verbose_name="Duracion Promedio del videojuego")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación",blank=True,null=True)

    class Meta:
        verbose_name = "videojuego"
        verbose_name_plural = "catalogopersonal"
        ordering = ["created"]

    def __str__(self):
        return self.title
