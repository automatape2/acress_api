from django.db import models

class Pubinei(models.Model):
    departamento = models.CharField(max_length=100, null=False, default="-")
    provincia = models.CharField(max_length=100, null=False, default="-")
    distrito = models.CharField(max_length=100, null=False, default="-")
    nombre = models.CharField(max_length=100, null=False, default="-")
    casos = models.IntegerField(null=False, default=0)
    porcentaje = models.FloatField(null=False, default=0.0)
    
    def __str__(self):
        return self.key
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'casos': self.casos,
            'porcetanje': self.porcentaje,
        }
        
        
class Poblacion(models.Model):
    departamento = models.CharField(max_length=100, null=False, default="-")
    provincia = models.CharField(max_length=100, null=False, default="-")
    distrito = models.CharField(max_length=100, null=False, default="-")
    idccpp = models.CharField(max_length=100, null=False, default="-")
    key = models.CharField(max_length=100, null=False, default="-")
    value = models.CharField(max_length=100, null=False, default="-")
    
    
     
        

