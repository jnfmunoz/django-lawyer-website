from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título", )
    subtitle = models.CharField(max_length=100, verbose_name="Subtítulo", )
    highlight_text = models.CharField(max_length=255, verbose_name="Texto Destacado")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    image = models.ImageField(upload_to='about/', verbose_name="Imagen")

    class Meta:
        verbose_name = "Acerca de"
        verbose_name_plural = "Acerca de"
        ordering = ["id"]
    
    def __str__(self) -> str:
        return self.title
