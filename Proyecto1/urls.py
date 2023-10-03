from django.contrib import admin
from django.urls import path, include
from Proyecto1.views import probando_template, origen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', probando_template),
    path('origen/<nombre>', origen),
    path('app-Proyecto/', include('AppProyecto.urls')),
]
