from .models import Pea2017

def get_pea2017(departamento, provincia, distrito):
    pubinei = Pea2017.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito
    ).all()
    print(departamento, provincia, distrito)
    return pubinei

    
def insert_pea(pea):
    pea.save()
    return pea
 