from django.db import models

class NBI(models.Model):
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    
    tipo = models.CharField(max_length=100)
    casos = models.IntegerField()
    porcentaje = models.FloatField()

    def __str__(self):
        return self.tipo
