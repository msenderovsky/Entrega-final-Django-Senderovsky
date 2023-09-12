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

def película(req, título, año, director, productora):
    director_obj = Director.objects.filter(apellido=director).first()
    productora_obj = Productora.objects.get(nombre=productora)
    película = Película(
        título=título, año=año, director=director_obj, productora=productora_obj
    )
    película.save()

    return HttpResponse(
        f"""<p> nombre: {película.título}, año: {película.año}, director: {película.director.nombre} {película.director.apellido}, productora: {película.productora.nombre} agregado</p>"""
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
            director_nombre= data["directorNombre"]
            director_apellido= data["directorApellido"]
            try:
                director = Director.objects.filter(nombre=director_nombre, apellido=director_apellido).first()
            except Director.DoesNotExist:
                director = Director(nombre=director_nombre, apellido=director_apellido)
                director.save()
            productora_nombre= data["productora"]
            try:
                productora = Productora.objects.get(nombre=productora_nombre)
            except Productora.DoesNotExist:
                productora = Productora(nombre=productora_nombre)
                productora.save()
            pelicula= Película(título= data["título"], año=data["año"], director=director, productora=productora)
            pelicula.save()
            return render(req,"inicio.html")
    else:
        miFormulario=PeliFormulario() 
        return render(req, "peliFormulario.html", {"miFormulario": miFormulario})
    return HttpResponse() 
    
def busquedaActor(req):
    metodo="busquedaActor"
    return render(req, "busquedaActor.html", {"metodo":metodo})

def busquedaDirector(req):
    metodo="busquedaDirector"
    return render(req, "busquedaDirector.html", {"metodo":metodo})

def busquedaPelicula(req):
    return render(req, "busquedaPelicula.html")

def buscar(req):
    if 'nombre' in req.GET and 'apellido' in req.GET:
        nombre= req.GET['nombre']
        apellido=req.GET['apellido']
        metodo= req.GET.get('metodo')
        if metodo=="busquedaActor":
            actores= Actor.objects.filter(nombre=nombre, apellido=apellido)
            return render(req, "resultadoBusqueda.html", {"actores": actores})
        elif metodo=="busquedaDirector":
            directores= Director.objects.filter(nombre=nombre, apellido=apellido)
            return render(req, "resultadoBusqueda.html", {"directores":directores})
    elif 'título' in req.GET:
        título= req.GET['título']
        peliculas= Película.objects.filter(título=título)
        return render(req, "resultadoBusqueda.html", {"peliculas": peliculas})
    return HttpResponse("No se encuentra lo que ésta buscando")