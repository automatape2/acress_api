from django.db import models

class SuSalud(models.Model):
    key = models.CharField(max_length=100)
    value = models.JSONField()
    
    def __str__(self):
        return self.key

class IPress(models.Model):
    key = models.CharField(max_length=900)
    value = models.JSONField()
    
    def __str__(self):
        return self.key