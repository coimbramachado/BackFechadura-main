from django.db import models
    

class fechadura(models.Model):

    id_fechadura = models.CharField(max_length=50)
    nome_fecha = models.CharField(max_length=50)
    senha_entrada = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=20)
    


class log_acess(models.Model):

    usuario = models.CharField()
    hora_abertura = models.DateField()
    id_fechadura = models.CharField()

