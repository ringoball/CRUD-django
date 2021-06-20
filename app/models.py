from django.db import models

# Create your models here.
class Filmes(models.Model):
    nome = models.CharField(max_length=150)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=40)
    ano = models.IntegerField()

