from django.db import models

class IDH(models.Model):
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    ubigeo = models.CharField(max_length=100,null=True, blank=True, default='')
    ranking = models.IntegerField(null=True, default=0)
    detalle = models.JSONField(null=True, blank=True, default={})
    
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo
