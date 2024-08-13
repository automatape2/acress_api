from .models import Pubinei, Poblacion

def get_pubinei(departamento, provincia, distrito):
    pubineis = Pubinei.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito
    ).all()
    return pubineis

def insert_pubineis(pubineis):
    for pubinei in pubineis:
        pubinei.save()
    
    return pubineis

def get_poblacion(idccpp: str):
    poblacion = Poblacion.objects.filter(
        idccpp__in=idccpp.split(",")
    ).all()

    return list(poblacion)
