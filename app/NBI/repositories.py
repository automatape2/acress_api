from app.NBI.models import NBI
 
def get_nbis(departamento, provincia, distrito):
    midis = NBI.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito,
    ).all()
    return midis
