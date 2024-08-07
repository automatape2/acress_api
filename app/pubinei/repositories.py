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

def get_poblacion(departamento, provincia, distrito, idccpp):
    poblacion = Poblacion.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito,
        idccpp=idccpp
    ).all()

    return list(poblacion)
