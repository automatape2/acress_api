from app.midis.models import CentrosPoblados, Midis
 
def get_centros_poblados(distrito, provincia, departamento, centros_poblados) -> CentrosPoblados:
    centros_poblados = CentrosPoblados.objects.filter(key=distrito + provincia + departamento + centros_poblados).first()
    return centros_poblados

def insert_centros_poblados(centro_poblados : CentrosPoblados) -> CentrosPoblados:
    centro_poblados.save()
    return centro_poblados

def get_midis(distrito, provincia, departamento, centropoblado) -> Midis:
    midis = Midis.objects.filter(key=distrito + provincia + departamento + centropoblado).first()
    return midis

def insert_midis(midis : Midis) -> Midis:
    midis.save()
    return midis