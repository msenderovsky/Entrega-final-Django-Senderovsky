from django.shortcuts import render
from .models import Película,Director,Productora,Actor
from django.http import HttpResponse

# Create your views here.
#def película(req, nombre,año):
 #   película= Película(nombre=nombre, año=año)
  #  película.save()
   # return HttpResponse(f"""<p> nombre: {película.nombre}, año: {película.año} agregado</p>""")

def película(req, nombre, año, director, productora):
    director_obj = Director.objects.get(apellido=director)
    productora_obj = Productora.objects.get(nombre=productora)
    película = Película(
        nombre=nombre, año=año, director=director_obj, productora=productora_obj
    )
    película.save()

    return HttpResponse(
        f"""<p> nombre: {película.nombre}, año: {película.año}, director: {película.director.nombre} {película.director.apellido}, productora: {película.productora.nombre} agregado</p>"""
    )


def listar_pelis(req):
    lista= Película.objects.all()
    return render(req, 'lista_pelis.html', {"lista_pelis": lista})

def actor(req, nombre, apellido):
    actor= Actor(nombre=nombre, apellido=apellido)
    actor.save()
    return HttpResponse(f"""<p> nombre: {actor.nombre}, año: {actor.apellido} agregado</p>""")

def productora(req, nombre):
    productora= Productora(nombre=nombre)
    productora.save()
    return HttpResponse(f"""<p> nombre: {productora.nombre} agregado</p>""")

def director(req, nombre, apellido):
    director= Director(nombre=nombre, apellido=apellido)
    director.save()
    return HttpResponse(f"""<p> nombre: {director.nombre}, año: {director.apellido} agregado</p>""")