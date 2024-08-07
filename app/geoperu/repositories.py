from .models import GeoPeru
 
def get_geoperu(departamento, provincia, distrito, idccpp):
    poblacion = GeoPeru.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito,
        idccpp=idccpp
    ).all()

    return list(poblacion)
