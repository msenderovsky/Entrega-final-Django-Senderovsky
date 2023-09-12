from django.db import models

# Create your models here.
class Actor (models.Model):
    nombre = models.CharField(max_length=10)
    apellido= models.CharField(max_length=10)
    #nacimiento= models.DateField()
    películas= models.ManyToManyField('Película')
   
class Productora (models.Model):
    nombre = models.CharField(max_length=10)
    #fundacion= models.DateField()
    
class Director (models.Model):
    nombre = models.CharField(max_length=10, default='Unknown')
    apellido= models.CharField(max_length=10, default='Unknown')
    #nacimiento= models.DateField()

class Película (models.Model):
    título = models.CharField(max_length=30)
    año= models.IntegerField()
    director= models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    productora= models.ForeignKey(Productora, on_delete=models.CASCADE, null=True)
    class Meta():
        unique_together= ('título', 'director')