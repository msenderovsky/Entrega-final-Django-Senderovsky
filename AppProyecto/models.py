from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone

class Actor (models.Model):
    nombre = models.CharField(max_length=10)
    apellido= models.CharField(max_length=25)
    películas= models.ManyToManyField('Película')
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Director (models.Model):
    nombre = models.CharField(max_length=10, default='Unknown')
    apellido= models.CharField(max_length=25, default='Unknown')
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Película (models.Model):
    título = models.CharField(max_length=30)
    director= models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    productora= models.CharField(max_length=10)
    class Meta():
        unique_together= ('título', 'director')
    def __str__(self):
        return self.título
        
class Critico(models.Model):
    nombre = models.CharField(max_length=10, default='Unknown')
    apellido = models.CharField(max_length=25, default='Unknown')
    email = models.EmailField(default="Unknown@unknown.com")
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        if not self.user:
            User = get_user_model()
            request = kwargs.pop('request', None)
            if request and request.user.is_authenticated:
                self.user = User.objects.get(username=request.user.username)
        super().save(*args, **kwargs)

class Critica(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50, default='Default')
    texto= models.TextField()
    fecha = models.DateTimeField(default=timezone.now, editable=False)
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)
    critico= models.ForeignKey(Critico, on_delete=models.CASCADE, null=True)
    pelicula= models.ForeignKey(Película, on_delete=models.CASCADE, null=True)