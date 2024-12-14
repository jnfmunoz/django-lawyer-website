from django.db import models
from fontawesome_5.fields import IconField
from core.utils.icon_formatter import get_practice_formatted_icon

class PracticeArea(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    icon = IconField(max_length=255, verbose_name="Icono", help_text="Clase de Font Awesome")

    def get_practice_formatted_icon(self):
        return get_practice_formatted_icon(self.icon)

    class Meta:
        verbose_name = "Área de Práctica"
        verbose_name_plural = "Áreas de Práctica"
        ordering = ["title"]

    def __str__(self):
        return f"Título: {self.title} | Descripción: {self.description} | Ícono: {self.icon}"

