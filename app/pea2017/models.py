from django.db import models

class Pea2017(models.Model):
    key = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pea_ocupada = models.CharField(max_length=100)
    pea_desocupada = models.CharField(max_length=100)
    no_pea = models.CharField(max_length=100)
    
    def __str__(self):
        return self.key
