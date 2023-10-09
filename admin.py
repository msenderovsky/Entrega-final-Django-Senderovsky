from django.contrib import admin
from .models import *

class ActorAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido']
    search_fields= ['nombre', 'apellido']
    
class DirectorAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido']
    search_fields= ['nombre', 'apellido']
    
class PeliAdmin(admin.ModelAdmin):
    list_display= ['título', 'director', 'productora']
    search_fields= ['título', 'director__apellido']
    list_filter= ['director', 'título']
    
class CriticoAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido', 'email', 'user']
    search_fields= ['nombre', 'apellido', 'email', 'user']
    list_filter= ['nombre', 'apellido', 'user']
    
class CriticaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'critico_apellido', 'critico_nombre', 'pelicula_titulo']
    search_fields= ['titulo', 'fecha', 'critico__apellido', 'pelicula_nombre']
    list_filter= ['pelicula__título', 'fecha', 'critico__apellido']

    def critico_apellido(self, obj):
        return obj.critico.apellido

    def critico_nombre(self, obj):
        return obj.critico.nombre

    def pelicula_titulo(self, obj):
        return obj.pelicula.título

    critico_apellido.short_description = 'Critico Apellido'
    critico_nombre.short_description = 'Critico Nombre'
    pelicula_titulo.short_description = 'Pelicula Título'

admin.site.register(Película, PeliAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Critico, CriticoAdmin)
admin.site.register(Critica, CriticaAdmin)