from django.contrib import admin
from .models import Película, Actor, Director, Productora

class ActorAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido']
    search_fields= ['nombre', 'apellido']
    
class DirectorAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido']
    search_fields= ['nombre', 'apellido']
    
class PeliAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'año', 'director', 'productora']
    search_fields= ['nombre', 'director']
    list_filter= ['director', 'año', 'nombre']

# Register your models here.
admin.site.register(Película, PeliAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Productora)