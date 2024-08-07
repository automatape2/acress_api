from django.db import models

class GeoPeru(models.Model):
    departamento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    idccpp = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.departamento} - {self.provincia} - {self.distrito} - {self.idccpp}"