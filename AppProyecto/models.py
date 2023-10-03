from django.db import models

class Actor (models.Model):
    nombre = models.CharField(max_length=10)
    apellido= models.CharField(max_length=10)
    películas= models.ManyToManyField('Película')
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Director (models.Model):
    nombre = models.CharField(max_length=10, default='Unknown')
    apellido= models.CharField(max_length=10, default='Unknown')
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Película (models.Model):
    título = models.CharField(max_length=30)
    director= models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    productora= models.CharField
    class Meta():
        unique_together= ('título', 'director')
        
class Critico (models.Model):
    nombre = models.CharField(max_length=10, default='Unknown')
    apellido= models.CharField(max_length=10, default='Unknown')
    email=models.EmailField()

class Critica(models.Model):
    titulo = models.CharField(max_length=30)
    texto= models.TextField()
    critico= models.ForeignKey(Critico, on_delete=models.CASCADE, null=True)
    pelicula= models.ForeignKey(Película, on_delete=models.CASCADE, null=True)
    
class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=10)
    email=models.EmailField()
