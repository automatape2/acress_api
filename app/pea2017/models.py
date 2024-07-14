from django.db import models

class Pea2017(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100, default=None, null=True)
    distrito = models.CharField(max_length=100, default=None, null=True)
    
    def __str__(self):
        return self.key