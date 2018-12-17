from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    telefono = models.TextField(verbose_name="Número de Contacto")
    FechaNacimiento= models.DateField( verbose_name="Fecha de Nacimiento")
    dni = models.TextField(verbose_name="Dni")
    
    def __str__(self): 
        return self.usuario.username
    
'''
#@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    '''

    
