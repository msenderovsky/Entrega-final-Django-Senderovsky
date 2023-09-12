from django.urls import path
from .views import inicio, película, actor, productora, director, listar_pelis, listar_actores, listar_directores, listar_productoras, actorFormulario, directorFormulario,peliFormulario, busquedaActor, busquedaDirector, busquedaPelicula, buscar

urlpatterns = [
    path('', inicio, name="inicio"),
    path('agrega-film/<título>/<año>/<director>/<productora>', película),
    path('agrega-actor/<nombre>/<apellido>/', actor),
    path('agrega-director/<nombre>/<apellido>/', director),
    path('agrega-productora/<nombre>/', productora),
    path('lista-pelis/', listar_pelis, name="lista_pelis"),
    path('lista-actores/', listar_actores, name="lista_actores"),
    path('lista-directores/', listar_directores, name="lista_directores"),
    path('lista-productoras/', listar_productoras, name="lista_productoras"),
    path('actor-formulario/', actorFormulario, name="actorFormulario"),
    path('director-formulario/', directorFormulario, name="directorFormulario"),
    path('película-formulario/', peliFormulario, name="peliFormulario"),
    path('busqueda-actor/', busquedaActor, name="busquedaActor"),
    path('busqueda-director/', busquedaDirector, name="busquedaDirector"),
    path('busqueda-pelicula/', busquedaPelicula, name="busquedaPelicula"),
    path('buscar/', buscar, name="buscar"),
]