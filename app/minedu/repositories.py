from .models import Minedu
 
def get_minedu(departamento, provincia, distrito):
    minedus = Minedu.objects.filter(
        departamento=departamento,
        provincia=provincia,
        distrito=distrito
        ).all()
    return minedus

def insert_minedu(minedus):
    for minedu in minedus:
        minedu.save()
    return minedus