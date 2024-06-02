from django.db import models

class CentrosPoblados(models.Model):
    key = models.CharField(max_length=100)
    value = models.JSONField()
    
    def __str__(self):
        return self.key

class Midis(models.Model):
    key = models.CharField(max_length=100)
    value = models.JSONField()
    
    def __str__(self):
        return self.key
