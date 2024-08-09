from django.db import models

class GeoPeru(models.Model):
    idccpp = models.CharField(max_length=50)
    indicador = models.CharField(max_length=500)
    poblacion = models.CharField(max_length=50)
    porcentaje = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.idccpp} - {self.indicador} - {self.poblacion} - {self.porcentaje}"