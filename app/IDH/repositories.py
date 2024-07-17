from app.IDH.models import IDH
 
def get_idhs(departamento, provincia, distrito):
    
    midis = IDH.objects.filter(
        departamento=departamento.upper(),
        provincia=provincia,
        distrito=distrito,
        ranking__gt=0,
    ).all()
    return midis
