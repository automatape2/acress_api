from django.db import models

class Minedu(models.Model):
    departamento = models.CharField(max_length=100, default=None, blank=True, null=False)
    provincia = models.CharField(max_length=100, default=None, blank=True, null=False)
    distrito = models.CharField(max_length=100, default=None, blank=True, null=False)
    
    nombre = models.CharField(max_length=100, default=None, blank=True, null=False)
    niveles = models.JSONField(default=None, blank=True, null=False)
    
    
    def __str__(self):
        return self.nombre
