from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
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

class ListarPeliculasActorID(ListView):
    model= Película
    template_name= "lista_peliculas_actor.html"
    context_object_name= "lista_peliculas"
    def get_queryset(self):
        actor_id = self.kwargs['pk']
        queryset = super().get_queryset()
        queryset = queryset.filter(actor__id=actor_id)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actor_id = self.kwargs['pk']
        actor = Actor.objects.get(id=actor_id)
        context['actor'] = actor
        return context
    
class ListarPeliculasDirectorID(ListView):
    model= Película
    template_name= "lista_peliculas_director.html"
    context_object_name= "lista_peliculas"
    def get_queryset(self):
        director_id = self.kwargs['pk']
        queryset = super().get_queryset()
        queryset = queryset.filter(director__id=director_id)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        director_id = self.kwargs['pk']
        director = Director.objects.get(id=director_id)
        context['director'] = director
        return context
        
class DetalleUsuario(DetailView):
    model:User
    template_name="detalleUsuario.html"
    context_object_name="user"

    def get_object(self, queryset=None):
        return self.request.user

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

class ActorCreationForm(forms.ModelForm):
    películas = forms.ModelMultipleChoiceField(queryset=Película.objects.all())

    class Meta:
        model = Actor
        fields = ['nombre', 'apellido', 'películas']

class CrearActor(StaffRequiredMixin, CreateView):
    model = Actor
    template_name = "crearActor.html"
    form_class = ActorCreationForm
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
    template_name = "crearPeli.html"
    fields=['título','director', 'productora' ]
    success_url='/app-Proyecto/lista-pelis/'
    def test_func(self):
        return self.request.user.is_staff

class CrearCritico(StaffRequiredMixin, CreateView):
    model = Critico
    template_name = "crearCritico.html"
    fields = ['nombre', 'apellido', 'email']
    success_url='/app-Proyecto/lista-criticos/'
    def test_func(self):
        return self.request.user.is_superuser
    def form_valid(self, form):
        form.instance.save(request=self.request)
        return redirect(self.success_url)

class CrearCritica(StaffRequiredMixin, CreateView):
    model = Critica
    template_name = "crearCritica.html"
    class CriticaForm(forms.ModelForm):
        class Meta:
            model = Critica
            fields = ['pelicula', 'titulo', 'subtitulo','texto', 'imagen']
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
        form.instance.critico = self.request.user.critico
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
    
class BorrarCuenta(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = "borrarCuenta.html"
    success_url = '/app-Proyecto/'
    context_object_name= "user"
    def get_object(self, queryset=None):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BorrarActor(StaffRequiredMixin, DeleteView):
    model = Actor
    template_name = "borrarActor.html"
    success_url = '/app-Proyecto/lista-actores'
    context_object_name= "actor"
    def test_func(self):
        return self.request.user.is_staff

class BorrarDirector(StaffRequiredMixin, DeleteView):
    model = Director
    template_name = "borrarDirector.html"
    success_url = '/app-Proyecto/lista-directores'
    context_object_name= "director"
    def test_func(self):
        return self.request.user.is_staff

class BorrarPelicula(StaffRequiredMixin, DeleteView):
    model = Película
    template_name = "borrarPelicula.html"
    success_url = '/app-Proyecto/lista-pelis'
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
    success_url = '/app-Proyecto/pages/'
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
            return render(req, "login.html", {"mensaje": f"Usuario {u} registrado correctamente"})
        return render(req, "registro.html", {"mensaje": f"Formulario inválido", "miFormulario": miFormulario})
    else:
        miFormulario=UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})

@login_required(login_url='login')
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
