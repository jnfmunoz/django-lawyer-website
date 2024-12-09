from django.db import models
from fontawesome_5.fields import IconField

# Create your models here.
class SocialNetwork(models.Model):
    icon = IconField(max_length=255, verbose_name="Icono", help_text="Clase de Font Awesome")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    link = models.URLField(verbose_name="Enlace", blank=True)

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ["id"]
    
    def __str__(self) -> str:
        return f"{self.description}"

"""
from django.db import models
from fontawesome_5.fields import IconField

class Contact(models.Model):
    CONTACT_CHOICES = [
        ("social", "Red Social"),
        ("phone", "Teléfono"),
        ("email", "Correo Electrónico"),
    ]
    
    social_type = models.CharField(
        max_length=10,
        choices=CONTACT_CHOICES,
        verbose_name="Tipo de Contacto",
        help_text="Selecciona el tipo de contacto (Red Social, Teléfono o Correo Electrónico)"
    )
    icon = IconField(
        max_length=255,
        verbose_name="Icono",
        help_text="Clase de Font Awesome para identificar visualmente el contacto"
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Descripción",
        help_text="Descripción del contacto (e.g., Facebook, WhatsApp, Correo Personal)"
    )
    social_value = models.CharField(
        max_length=255,
        verbose_name="Contacto",
        help_text="URL, número de teléfono o correo electrónico"
    )

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.description}: {self.value}"
"""