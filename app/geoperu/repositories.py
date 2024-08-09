from .models import GeoPeru
 
def get_geoperus(idccpp):
    geoperus = GeoPeru.objects.filter(
        idccpp=idccpp,
        indicador__contains="Lengua materna:"
    ).all()

    return list(geoperus)
