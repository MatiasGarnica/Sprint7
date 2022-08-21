from django.contrib import admin
from .models import Proyectos

# Register your models here.
#Le decimos que los campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
admin.site.register(Proyectos)