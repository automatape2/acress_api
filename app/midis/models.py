from django.db import models

class CentrosPoblados(models.Model):
    key = models.CharField(max_length=100)
    value = models.JSONField()
    
    def __str__(self):
        return self.key

class Midis(models.Model):
    departamento = models.CharField(max_length=100, default=None, blank=True, null=False)
    provincia = models.CharField(max_length=100, default=None, blank=True, null=False)
    distrito = models.CharField(max_length=100, default=None, blank=True, null=False)
    centro_poblado = models.CharField(max_length=100, default=None, blank=True, null=False)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    
    def __str__(self):
        return self.key
