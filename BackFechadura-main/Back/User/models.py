from django.db import models


# Create your models here.
class user(
    
    nome = models.CharField(max_length=50)
    sobre_nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    chave_publi = models.CharField(max_length=250)

