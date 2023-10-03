from django.contrib import admin
from .models import Película, Actor, Director

class ActorAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido']
    search_fields= ['nombre', 'apellido']
    
class DirectorAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido']
    search_fields= ['nombre', 'apellido']
    
class PeliAdmin(admin.ModelAdmin):
    list_display= ['título', 'director', 'productora']
    search_fields= ['título', 'director']
    list_filter= ['director', 'título']

admin.site.register(Película, PeliAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)