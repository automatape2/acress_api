from .models import Pea2017

def get_pea2017(departamento, province, district):
    pubinei = Pea2017.objects.filter(departamento=departamento,provincia=province,distrito=district).all()
    return pubinei

    
def insert_pea(pea):
    pea.save()
    return pea
 