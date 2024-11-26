from typing import Any
from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.CharField(max_length=200, verbose_name="Descripción")

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"
        ordering = ["id"]
    
    def __str__(self) -> str:
        return self.title