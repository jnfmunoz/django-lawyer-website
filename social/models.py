from django.db import models
from fontawesome_5.fields import IconField

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, EmailValidator
import re

# Create your models here.
class SocialNetwork(models.Model):
    CONTACT_CHOICES = [
        ("social", "Red Social"),
        ("phone", "Teléfono"),
        ("email", "Correo Electrónico"),
    ]

    icon = IconField(max_length=255, 
                     verbose_name="Icono", 
                     help_text="Clase de Font Awesome")    
    description = models.CharField(max_length=200, 
                                    verbose_name="Descripción")    
    social_type = models.CharField(max_length=10, 
                                    choices=CONTACT_CHOICES, 
                                    verbose_name="Tipo de Contacto", 
                                    help_text="Selecciona el tipo de contacto (Red Social, Teléfono o Correo Electrónico)")    
    social_value = models.CharField(max_length=255,
                                    verbose_name="Contacto",
                                    help_text="URL, número de teléfono o correo electrónico")

    # Validaciones del modelo
    def clean(self):
        super().clean() # llamamos la método ´clean´ de la clase 
        if self.social_type == "social":
            # Validar si corresponde a un enlace
            url_validator = URLValidator()
            value = self.social_value.strip()
            
            # Asegurar que tenga esquema (http o https)
            if not value.startswith(("http://", "https://")): # Usa una tupla
                value = f'https://{value}'
            try:
                # url_validator(self.social_value)
                url_validator(value)
            except ValidationError:
                raise ValidationError({
                    'social_value' : 'Debe ser una URL válida para una red social' 
                    })
            
            # Actualiza el atributo
            self.social_value = value

    def formated_icon(self):
        """
        Retorna el campo `icon` formateado correctamente para usar en el template.
        """
        icon_value = str(self.icon) # Convertir a cadena
        parts = [part.strip() for part in icon_value.split(',')] # Separar y limpiar las partes
        
        # Crear lista de clases para asignar el tamaño fa-2x
        formatted_icon = []

        # Recorrer las partes y verificar si hay un prefijo de tipo de icono (fab, fas, etc.)
        # for part in parts:
            

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ["id"]

    def __str__(self) -> str: 
        return f"{self.description} : {self.social_value}"
    


