from django.db import models

class SuSalud(models.Model):
    key = models.CharField(max_length=100)
    value = models.JSONField()
    
    def __str__(self):
        return self.key

class IPress(models.Model):
    departamento = models.CharField(max_length=900, null=False, blank=True, default=None)
    provincia = models.CharField(max_length=900, null=False, blank=True, default=None)
    distrito = models.CharField(max_length=900, null=False, blank=True, default=None)
    key = models.CharField(max_length=900, null=False, blank=True, default=None)
    value = models.JSONField()
    
    def __str__(self):
        return self.key