from django.shortcuts import render
from django.http import HttpResponse
from .models import Película,Director,Productora,Actor
from .forms import ActorFormulario, DirectorFormulario, PeliFormulario

# Create your views here.
#def película(req, nombre,año):
 #   película= Película(nombre=nombre, año=año)
  #  película.save()
   # return HttpResponse(f"""<p> nombre: {película.nombre}, año: {película.año} agregado</p>""")

def inicio(req):
    return render(req,'inicio.html')

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

def listar_actores(req):
    lista= Actor.objects.all()
    return render(req, 'lista_actores.html', {"lista_actores": lista})

def productora(req, nombre):
    productora= Productora(nombre=nombre)
    productora.save()
    return HttpResponse(f"""<p> nombre: {productora.nombre} agregado</p>""")

def listar_productoras(req):
    lista= Productora.objects.all()
    return render(req, 'lista_productoras.html', {"lista_productoras": lista})

def director(req, nombre, apellido):
    director= Director(nombre=nombre, apellido=apellido)
    director.save()
    return HttpResponse(f"""<p> nombre: {director.nombre}, año: {director.apellido} agregado</p>""")

def listar_directores(req):
    lista= Director.objects.all()
    return render(req, 'lista_directores.html', {"lista_directores": lista})

def actorFormulario(req):

    if (req.method== 'POST'):
        miFormulario= ActorFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            actor= Actor(nombre= data["nombre"], apellido=data["apellido"])
            actor.save()
            return render(req,"inicio.html")
    else:
        miFormulario=ActorFormulario() 
        return render(req, "actorFormulario.html", {"miFormulario": miFormulario})
    
def directorFormulario(req):

    if (req.method== 'POST'):
        miFormulario= DirectorFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            director= Director(nombre= data["nombre"], apellido=data["apellido"])
            director.save()
            return render(req,"inicio.html")
    else:
        miFormulario=DirectorFormulario() 
        return render(req, "directorFormulario.html", {"miFormulario": miFormulario})
    
def peliFormulario(req):

    if (req.method== 'POST'):
        miFormulario= PeliFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            pelicula= Película(nombre= data["nombre"], año=data["año"], director=data["director"], productora=data["productora"])
            pelicula.save()
            return render(req,"inicio.html")
    else:
        miFormulario=DirectorFormulario() 
        return render(req, "peliculaFormulario.html", {"miFormulario": miFormulario})
    
def busquedaActor(req):
    return render(req, "busquedaActor.html")

def busquedaDirector(req):
    return render(req, "busquedaDirector.html")

def busquedaPelicula(req):
    return render(req, "busquedaPelicula.html")

def buscar(req):
    if req.GET['nombre'] and req.GET['apellido']:
        nombre= req.GET['nombre']
        apellido=req.GET['apellido']
        actores= Actor.objects.filter(nombre=nombre, apellido=apellido)
        return render(req, "resultadoBusqueda.html", {"actores": actores})
    elif req.GET['nombre'] and req.GET['año']:
        nombre= req.GET['nombre']
        año=req.GET['año']
        peliculas= Película.objects.filter(nombre=nombre, año=año)
        return render(req, "resultadoBusqueda.html", {"peliculas": peliculas})
    else:
        return HttpResponse("No se encuentra el actor buscado")