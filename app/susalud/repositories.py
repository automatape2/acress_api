from .models import SuSalud, IPress

def get_ipresses(departamento, provincia, distrito):
    ipresses = IPress.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito
    ).all()
    return ipresses

def get_susalud(distrito, provincia, departamento) -> SuSalud:
    susalud = SuSalud.objects.filter(key=distrito + provincia + departamento).first()
    return susalud

def insert_ipresses(ipresses):
    for ipress in ipresses:
        ipress.save()
    
    return ipresses

def insert_susalud(susalud : SuSalud) -> SuSalud:
    susalud.save()
    return susalud