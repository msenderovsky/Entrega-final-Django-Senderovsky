from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Proyecto1.views import probando_template, origen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', probando_template),
    path('origen/<nombre>', origen),
    path('app-Proyecto/', include('AppProyecto.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
