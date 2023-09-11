from django.urls import path
from .views import inicio, película, actor, productora, director, listar_pelis, listar_actores, listar_directores, listar_productoras

urlpatterns = [
    path('', inicio),
    path('agrega-film/<nombre>/<año>/<director>/<productora>', película),
    path('lista-pelis/', listar_pelis),
    path('lista-actores/', listar_actores),
    path('lista-directores/', listar_directores),
    path('lista-productoras/', listar_productoras),
    path('agrega-actor/<nombre>/<apellido>/', actor),
    path('agrega-director/<nombre>/<apellido>/', director),
    path('agrega-productora/<nombre>/', productora),
]