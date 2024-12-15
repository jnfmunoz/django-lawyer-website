from django.db import models
from fontawesome_5.fields import IconField
from core.utils.icon_formatter import get_social_network_formatted_icon

# Create your models here.
class SocialNetwork(models.Model):
    description = models.CharField(max_length=200, 
                                    verbose_name="Descripción")    
    icon = IconField(max_length=255, 
                     verbose_name="Icono", 
                     help_text="Clase de Font Awesome")    
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Enlace", help_text="URL Red Social")

    def get_social_network_formatted_icon(self):
        return get_social_network_formatted_icon(self.icon)
            
    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ["id"]

    def __str__(self) -> str: 
        return f"{self.description}"

class Address(models.Model):
    street = models.CharField(max_length=200, 
                             verbose_name="Calle")
    number = models.IntegerField(verbose_name="Número")
    commune = models.CharField(max_length=200,
                               verbose_name="Comuna")
    country = models.CharField(max_length=200,
                               verbose_name="País")

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Dirección"
        ordering = ["id"]
    
    def __str__(self) -> str:
        return f"{self.street} {self.number}, {self.commune}, {self.country}"
    
class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, 
                                    verbose_name="Número de Teléfono")
    email = models.EmailField(max_length=200, 
                              verbose_name="Correo electrónico")
    
    class Meta:
        verbose_name = "Información de Contacto"
        verbose_name_plural = "Información de Contacto"
        ordering = ["id"]
    
    def __str__(self) -> str:
        return f"N° Teléfono: {self.phone_number} | Correo electrónico: {self.email}"