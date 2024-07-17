from app.midis.models import CentrosPoblados, Midis
 
def get_centros_poblados(distrito, provincia, departamento, centros_poblados) -> CentrosPoblados:
    centros_poblados = CentrosPoblados.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito,
        centros_poblados=centros_poblados,
        ).all()
    return centros_poblados

def insert_centros_poblados(centro_poblados : CentrosPoblados) -> CentrosPoblados:
    centro_poblados.save()
    return centro_poblados

def get_midis(distrito, provincia, departamento, centropoblado) -> Midis:
    midis = Midis.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito,
        centro_poblado=centropoblado,
        ).all()
    return midis

def insert_midis(midis):
    for midi in midis:
        midi.save()
    return midis