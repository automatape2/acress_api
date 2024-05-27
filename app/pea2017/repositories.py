from .models import Pea2017

def get_pea2017(departamento):
    pubinei = Pea2017.objects.filter(codigo=departamento).first()
    return pubinei

    
def insert_pea(pea):
    pea.save()
    return pea
 