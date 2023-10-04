from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

class StaffRequiredMixin(UserPassesTestMixin):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def inicio(req):
    return render(req,'inicio.html')

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

class ListarCriticasID(ListView):
    model= Critica
    template_name= "lista_criticas_id.html"
    context_object_name= "lista_criticas"
    def get_queryset(self):
        pelicula_id = self.kwargs['pk']
        queryset = super().get_queryset()
        queryset = queryset.filter(pelicula__id=pelicula_id)
        return queryset

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
    pk_url_kwarg = "pk"

class CrearActor(StaffRequiredMixin, CreateView):
    model = Actor
    template_name = "crearActor.html"
    fields=['nombre','apellido','peliculas']
    success_url='/app-Proyecto/lista-actores/'
    def test_func(self):
        return self.request.user.is_staff

class CrearDirector(StaffRequiredMixin, CreateView):
    model = Director
    template_name = "crearDirector.html"
    fields=['nombre','apellido']
    success_url='/app-Proyecto/lista-directores/'
    def test_func(self):
        return self.request.user.is_staff

class CrearPelicula(StaffRequiredMixin, CreateView):
    model = Película
    template_name = "peliFormulario.html"
    fields=['título','director', 'productora' ]
    success_url='/app-Proyecto/lista-pelis/'
    def test_func(self):
        return self.request.user.is_staff

class CrearCritico(StaffRequiredMixin, CreateView):
    model = Critico
    template_name = "crearCritico.html"
    fields=['nombre','apellido','email']
    success_url='/app-Proyecto/lista-criticos/'
    def test_func(self):
        return self.request.user.is_staff

class CrearCritica(StaffRequiredMixin, CreateView):
    model = Critica
    template_name = "crearCritica.html"
    class CriticaForm(forms.ModelForm):
        '''critico_nombre = forms.CharField(
            max_length=30,
            label='Nombre del Crítico',
            required=False,
        )
        critico_apellido = forms.CharField(
            max_length=30,
            label='Apellido del Crítico',
            required=False,
        )'''
        class Meta:
            model = Critica
            fields = ['pelicula', 'titulo', 'texto']
    form_class = CriticaForm
    success_url='/app-Proyecto/pages/'
    def test_func(self):
        return self.request.user.is_staff
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula_id = self.kwargs['pk']
        pelicula = get_object_or_404(Película, id=pelicula_id)
        context['pelicula'] = pelicula
        return context

    def form_valid(self, form):
        form.instance.pelicula = self.get_context_data()['pelicula']
        return super().form_valid(form)

class ActualizarActor(StaffRequiredMixin, UpdateView):
    model = Actor
    template_name = "actualizarActor.html"
    fields=('__all__')
    success_url='/app-Proyecto/lista-actores/'
    context_object_name= "actor"
    def test_func(self):
        return self.request.user.is_staff

class ActualizarDirector(StaffRequiredMixin, UpdateView):
    model = Director
    template_name = "actualizarDirector.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-directores/'
    context_object_name= "director"
    def test_func(self):
        return self.request.user.is_staff

class ActualizarPelicula(StaffRequiredMixin, UpdateView):
    model = Película
    template_name = "actualizarPelicula.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-pelis/'
    context_object_name= "pelicula"
    def test_func(self):
        return self.request.user.has_perm('app-Proyecto.can_edit_pelicula')

class ActualizarCritico(StaffRequiredMixin, UpdateView):
    model = Critico
    template_name = "actualizarCritico.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-criticos/'
    context_object_name= "critico"
    def test_func(self):
        return self.request.user.is_staff

class ActualizarCritica(StaffRequiredMixin, UpdateView):
    model = Critica
    template_name = "actualizarCritica.html"
    fields='__all__'
    success_url='/app-Proyecto/lista-criticas/'
    context_object_name= "critica"
    def test_func(self):
        return self.request.user.is_staff

class BorrarActor(StaffRequiredMixin, DeleteView):
    model = Actor
    template_name = "borrarActor.html"
    success_url='/app-Proyecto/lista-actores/'
    context_object_name= "actor"
    def test_func(self):
        return self.request.user.is_staff

class BorrarDirector(StaffRequiredMixin, DeleteView):
    model = Director
    template_name = "borrarDirector.html"
    success_url='/app-Proyecto/lista-directores/'
    context_object_name= "director"
    def test_func(self):
        return self.request.user.is_staff

class BorrarPelicula(StaffRequiredMixin, DeleteView):
    model = Película
    template_name = "borrarPelicula.html"
    success_url='/app-Proyecto/lista-pelis/'
    context_object_name= "pelicula"
    def test_func(self):
        return self.request.user.is_staff

class BorrarCritico(StaffRequiredMixin, DeleteView):
    model = Critico
    template_name = "borrarCritico.html"
    success_url='/app-Proyecto/lista-criticos/'
    context_object_name= "critico"
    def test_func(self):
        return self.request.user.is_staff

class BorrarCritica(StaffRequiredMixin, DeleteView):
    model = Critica
    template_name = "borrarCritica.html"
    success_url='/app-Proyecto/lista-criticas'
    context_object_name= "critica"
    def test_func(self):
        return self.request.user.is_staff

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

def loginView(req):
    if req.method=='POST':
        miFormulario=AuthenticationForm(req, data=req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            u=data["username"]
            p=data["password"]
            user=authenticate(username=u, password=p)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {u}"})

        return render(req, "login.html", {"miFormulario": miFormulario, "mensaje": f"Datos incorrectos de inicio de sesión"})
    else:
        miFormulario=AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
def register(req):
    if req.method=='POST':
        miFormulario=UserCreationForm(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            u=data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {u} registrado correctamente"})
        return render(req, "registro.html", {"mensaje": f"Formulario inválido"})
    else:
        miFormulario=UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
    
def editar_perfil(req):
    usuario= req.user
    if usuario:
        if (req.method== 'POST'):
            miFormulario= UserEditForm(req.POST, instance=req.user)
            if miFormulario.is_valid(): 
                data= miFormulario.cleaned_data
                usuario.username= data["username"]
                usuario.email= data["email"]
                usuario.set_password(data["password1"])
                usuario.save()
                return render(req,"inicio.html",{ "mensaje": f"Datos actualizados con éxito"})
            else:
                return render(req, "editar_perfil.html", {"miFormulario": miFormulario})

        else:
            miFormulario=UserEditForm(instance=usuario) 
            return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
    else:
        return render(req, "login.html", {"miFormulario": miFormulario})

def about(req):
    return render(req,'about.html')

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