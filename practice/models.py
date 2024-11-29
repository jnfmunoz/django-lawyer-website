# from django.db import models
# from django.core.exceptions import ValidationError
# from fontawesome_5.fields import IconField

# # Create your models here.
# class PracticeArea(models.Model):
#     title = models.CharField(max_length=100, verbose_name="Título", )
#     description = models.CharField(max_length=200, verbose_name="Descripción")
#     icon = IconField(max_length=255, verbose_name="icono", help_text="Clase de Font Awesome")

#     def clean(self):
#         icon_value = str(self.icon)

#         icon_value = ' '.join(icon_value.split(','))

#         self.icon = icon_value

#         if ',' in icon_value:
#             raise ValidationError("El icono debe estar separado por espacios, no por comas.")
#         self.icon = ' '.join(self.icon.split(','))
    
#     class Meta:
#         verbose_name = "Área de Práctica"
#         verbose_name_plural = "Áreas de Práctica"
#         ordering = ["id"]
#     def __str__(self) -> str:
#         return self.title    

from django.db import models
from django.core.exceptions import ValidationError
from fontawesome_5.fields import IconField

class PracticeArea(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    icon = IconField(max_length=255, verbose_name="icono", help_text="Clase de Font Awesome")

    def clean(self):
        # Convertir el icono en una cadena y manejar espacios o comas
        icon_value = str(self.icon).strip()  # Eliminar espacios extras
        if ' ' in icon_value:
            icon_value = icon_value.replace(' ', '-')  # Reemplazar espacios con guiones

        if ',' in icon_value:
            icon_value = icon_value.replace(',', ' ')  # Reemplazar comas con espacios

        # Asegurar que el icono empiece con 'fa-' si no lo tiene
        if not icon_value.startswith('fa-'):
            icon_value = 'fa-' + icon_value  # Asegurar el prefijo correcto
        if icon_value.startswith('fas'):
            icon_value = 'fa-' + icon_value[4:]  # Reemplaza 'fas' por 'fa-'

        self.icon = icon_value  # Asignar el icono limpio

        if ',' in self.icon:
            raise ValidationError("El icono debe estar separado por espacios, no por comas.")

    class Meta:
        verbose_name = "Área de Práctica"
        verbose_name_plural = "Áreas de Práctica"
        ordering = ["id"]

    def __str__(self):
        return self.title



# class PracticeArea(models.Model):
#     title = models.CharField(max_length=100, verbose_name="Título")
#     description = models.CharField(max_length=200, verbose_name="Descripción")
#     icon = IconField(max_length=255, verbose_name="Icono", help_text="Clase de Font Awesome")

#     def clean(self):
#         """
#         Limpia y valida el campo icon para asegurarse de que no contenga comas y tenga un formato correcto.
#         """
#         if self.icon:
#             # Reemplazar comas por espacios y limpiar espacios redundantes
#             cleaned_icon = ' '.join(str(self.icon).split(',')).strip()

#             # Validar que no queden comas
#             if ',' in cleaned_icon:
#                 raise ValidationError({"icon": "El icono debe estar separado por espacios, no por comas."})

#             self.icon = cleaned_icon

#     def save(self, *args, **kwargs):
#         """
#         Sobrescribe el método save para limpiar y validar el campo icon antes de guardar.
#         """
#         self.clean()  # Llama al método clean para limpiar el campo
#         super().save(*args, **kwargs)  # Guarda el modelo

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Área de Práctica"
#         verbose_name_plural = "Áreas de Práctica"
#         ordering = ["id"]
