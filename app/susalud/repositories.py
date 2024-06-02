from .models import SuSalud, IPress

def get_ipress(idipress) -> IPress:
    ipress = IPress.objects.filter(key=idipress).first()
    return ipress

def get_susalud(distrito, provincia, departamento) -> SuSalud:
    susalud = SuSalud.objects.filter(key=distrito + provincia + departamento).first()
    return susalud

def insert_ipress(ipress : IPress) -> IPress:
    ipress.save()
    return ipress

def insert_susalud(susalud : SuSalud) -> SuSalud:
    susalud.save()
    return susalud