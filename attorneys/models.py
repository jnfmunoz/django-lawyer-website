from typing import Any
from django.db import models

# Create your models here.
class Attorney(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Primer nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    practice_area = models.CharField(max_length=100, verbose_name="Área de Práctica")
    twitter = models.URLField(verbose_name="Twitter", max_length=200, null=True, blank=True)
    facebook = models.URLField(verbose_name="Facebook", max_length=200, null=True, blank=True)
    linkedin = models.URLField(verbose_name="LinkedIn", max_length=200, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='attorneys/', verbose_name="Foto de perfil", blank=True)

    class Meta:
        verbose_name = "Abogado"
        verbose_name_plural = "Abogados"
        ordering = ["id"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"