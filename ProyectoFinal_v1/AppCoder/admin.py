from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Curso)
admin.site.register(models.Profesor)
admin.site.register(models.Pais)
admin.site.register(models.Cliente)
