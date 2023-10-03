from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import Película,Director,Actor,Critico, Critica
from .forms import ActorFormulario, DirectorFormulario, PeliFormulario, CriticoFormulario, CriticaFormulario

def inicio(req):
    return render(req,'inicio.html')
'''
def película(req, título, año, director, productora):
    director_obj = Director.objects.filter(apellido=director).first()
    productora = productora
    película = Película(
        título=título, año=año, director=director_obj, productora=productora
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

def director(req, nombre, apellido):
    director= Director(nombre=nombre, apellido=apellido)
    director.save()
    return HttpResponse(f"""<p> nombre: {director.nombre}, año: {director.apellido} agregado</p>""")

def listar_actores(req):
    lista= Actor.objects.all()
    return render(req, 'lista_actores.html', {"lista_actores": lista})

def listar_directores(req):
    lista= Director.objects.all()
    return render(req, 'lista_directores.html', {"lista_directores": lista})

def listar_criticos(req):
    lista= Critico.objects.all()
    return render(req, 'lista_criticos.html', {"lista_criticos": lista})

def listar_criticas(req):
    lista= Critica.objects.all()
    return render(req, 'lista_criticas.html', {"lista_criticos": lista})

'''
class ListarActores(ListView):
    model= Actor
    template_name= "lista_actores.html"
    context_object_name= "lista_actores"
    
class ListarDirectores(ListView):
    model= Director
    template_name= "lista_directores.html"
    context_object_name= "lista_directores"

class ListarPelis(ListView):
    model= Película
    template_name= "lista_pelis.html"
    context_object_name= "lista_pelis"
    
class ListarCriticos(ListView):
    model= Critico
    template_name= "lista_criticos.html"
    context_object_name= "lista_criticos"

class ListarCriticas(ListView):
    model= Critica
    template_name= "lista_criticas.html"
    context_object_name= "lista_criticas"

class DetalleActor(DetailView):
    model = Actor
    template_name = "detalleActor.html"
    context_object_name= "actor"
    
class DetalleDirector(DetailView):
    model = Director
    template_name = "detalleDirector.html"
    context_object_name= "director"
    
class DetallePelicula(DetailView):
    model = Película
    template_name = "detallePelicula.html"
    context_object_name= "pelicula"
    
class DetalleCritico(DetailView):
    model = Critico
    template_name = "detalleCritico.html"
    context_object_name= "critico"

class DetalleCritica(DetailView):
    model = Critica
    template_name = "detalleCritica.html"
    context_object_name= "critica"

class CrearActor(CreateView):
    model = Actor
    template_name = "crearActor.html"
    fields=['nombre','apellido','peliculas']
    success_url='/app-Proyecto/lista-actores/'
    
class CrearDirector(CreateView):
    model = Director
    template_name = "crearDirector.html"
    fields=['nombre','apellido']
    success_url='/app-Proyecto/lista-directores/'
    
class CrearPelicula(CreateView):
    model = Película
    template_name = "crearPeli.html"
    fields=['titulo','director__apellido', 'director__nombre', 'productora' ]
    success_url='/app-Proyecto/lista-pelis/'
    
class CrearCritico(CreateView):
    model = Critico
    template_name = "crearCritico.html"
    fields=['nombre','apellido','email']
    success_url='/app-Proyecto/lista-criticos/'
    
class CrearCritica(CreateView):
    model = Critica
    template_name = "crearCritica.html"
    fields=['pelicula__nombre','titulo','texto']
    success_url='/app-Proyecto/lista-criticas/'
    
class ActualizarActor(UpdateView):
    model = Actor
    template_name = "actualizarActor.html"
    fields=('__all__')
    success_url='/app-Proyecto/lista-actores/'
    context_object_name= "actor"
    
class ActualizarDirector(UpdateView):
    model = Director
    template_name = "actualizarDirector.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-directores/'
    context_object_name= "director"
    
class ActualizarPelicula(UpdateView):
    model = Película
    template_name = "actualizarPelicula.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-pelis/'
    context_object_name= "pelicula"
    
class ActualizarCritico(UpdateView):
    model = Critico
    template_name = "actualizarCritico.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-criticos/'
    context_object_name= "critico"
    
class ActualizarCritica(UpdateView):
    model = Critica
    template_name = "actualizarCritica.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-criticas/'
    context_object_name= "critica"

class BorrarActor(DeleteView):
    model = Actor
    template_name = "borrarActor.html"
    success_url='/app-Proyecto/lista-actores/'
    
class BorrarDirector(DeleteView):
    model = Director
    template_name = "borrarDirector.html"
    success_url='/app-Proyecto/lista-directores/'
    
class BorrarPelicula(DeleteView):
    model = Película
    template_name = "borrarPelicula.html"
    success_url='/app-Proyecto/lista-pelis/'
    
class BorrarCritico(DeleteView):
    model = Critico
    template_name = "borrarCritico.html"
    success_url='/app-Proyecto/lista-criticos/'
    
class BorrarCritica(DeleteView):
    model = Critica
    template_name = "borrarCritica.html"
    success_url='/app-Proyecto/lista-criticas'

'''

def crea_actor(req):
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
    
def crea_director(req):
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
    
def crea_peli(req):
    if (req.method== 'POST'):
        miFormulario= PeliFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            director_nombre= data["directorNombre"]
            director_apellido= data["directorApellido"]
            try:
                director = Director.objects.get(nombre=director_nombre, apellido=director_apellido)
                #director = Director.objects.filter(nombre=director_nombre, apellido=director_apellido).first()
            except Director.DoesNotExist:
                director = Director(nombre=director_nombre, apellido=director_apellido)
                director.save()
            productora= data["productora"]
            pelicula= Película(título= data["título"], año=data["año"], director=director, productora=productora)
            pelicula.save()
            return render(req,"inicio.html")
    else:
        miFormulario=PeliFormulario() 
        return render(req, "peliFormulario.html", {"miFormulario": miFormulario})
    return HttpResponse() 

def crear_critico(req):
    if (req.method== 'POST'):
        miFormulario= CriticoFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            critico= Critico(nombre= data["nombre"], apellido=data["apellido"], email=data["email"])
            critico.save()
            return render(req,"inicio.html")
    else:
        miFormulario=CriticoFormulario() 
        return render(req, "criticoFormulario.html", {"miFormulario": miFormulario})
    
def crear_critica(req):
    if (req.method== 'POST'):
        miFormulario= CriticaFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            critico_nombre= data["criticoNombre"]
            critico_apellido= data["criticoApellido"]
            try:
                critico = Critico.objects.get(nombre=critico_nombre, apellido=critico_apellido)
            except Critico.DoesNotExist:
                critico = Critico(nombre=critico_nombre, apellido=critico_apellido)
                critico.save()
            critica= Critica(titulo= data["titulo"], texto=data["texto"], pelicula=data["pelicula"], critico=critico)
            critica.save()
            return render(req,"inicio.html")
    else:
        miFormulario=CriticoFormulario() 
        return render(req, "criticaFormulario.html", {"miFormulario": miFormulario})

def eliminar_critico(req):
    if (req.method== 'POST'):
        critico= Critico.objects.get(id=id)
        critico.delete()
        lista= Critico.objects.all()
        return render(req, 'lista_criticos.html', {"lista_criticos": lista})

def eliminar_critica(req):
    if (req.method== 'POST'):
        critica= Critica.objects.get(id=id)
        critica.delete()
        lista= Critica.objects.all()
        return render(req, 'lista_criticas.html', {"lista_criticas": lista})

def editar_critico(req):
    critico= Critico.objects.get(id=id)
    if (req.method== 'POST'):
        miFormulario= CriticoFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            critico.nombre=data["nombre"]
            critico.apellido=data["apellido"]
            critico.email=data["email"]
            critico.save()
            return render(req,"inicio.html")
    else:
        miFormulario=CriticoFormulario(initial={ 
            "nombre":critico.nombre,
            "apellido":critico.apellido,
            "email":critico.email,
        })
        return render(req, "editarCritico.html", {"miFormulario": miFormulario, "id": critico.id})

def editar_critica(req):
    critica= Critica.objects.get(id=id)
    if (req.method== 'POST'):
        miFormulario= CriticaFormulario(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            critica.titulo=data["titulo"]
            critica.texto=data["texto"]
            critica.pelicula=data["pelicula"]
            critico_nombre= data["criticoNombre"]
            critico_apellido= data["criticoApellido"]
            try:
                critico = Critico.objects.get(nombre=critico_nombre, apellido=critico_apellido)
            except Critico.DoesNotExist:
                critico = Critico(nombre=critico_nombre, apellido=critico_apellido)
                critico.save()
            critica= Critica(titulo= data["titulo"], texto=data["texto"], pelicula=data["pelicula"], critico=critico)
            critica.save()
            return render(req,"inicio.html")
    else:
        miFormulario=CriticoFormulario(initial={ 
            "titulo":critica.titulo,
            "texto":critica.texto,
            "critico":critica.critico,
            "pelicula":critica.pelicula
        })
        return render(req, "editarCritica.html", {"miFormulario": miFormulario, "id": critica.id})
'''
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

def busquedaActor(req):
    metodo="busquedaActor"
    return render(req, "busquedaActor.html", {"metodo":metodo})

def busquedaDirector(req):
    metodo="busquedaDirector"
    return render(req, "busquedaDirector.html", {"metodo":metodo})

def busquedaPelicula(req):
    return render(req, "busquedaPelicula.html")

def busquedaCritico(req):
    return render(req, "busquedaCritico.html")

def busquedaCritica(req):
    return render(req, "busquedaCritica.html")

def login(req):
    critico= Critico.objects.get(id=id)
    if req.method=='POST':
        miFormulario=CriticoFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            critico.nombre=data["nombre"]
            critico.apellido=data["apellido"]
            critico.email=data["email"]
            critico.save()
            return render(req, "inicio.html")
    else:
        miFormulario=CriticoFormulario(initial={ 
            "nombre":critico.nombre,
            "apellido":critico.apellido,
            "email":critico.email,
        })
        return render(req, "editarCritico.html", {"miFormulario": miFormulario, "id": critico.id})
