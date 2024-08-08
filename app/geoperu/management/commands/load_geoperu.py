from django.core.management.base import BaseCommand
from app.geoperu.services import get_pubinei_from_web

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        codigo_departamento = "01"
        codigo_provincia = "01"
        codigo_distrito = "01"
        codigo_centropoblado = "0001"

        idccpp = codigo_departamento + codigo_provincia + codigo_distrito + codigo_centropoblado

        geoperu = get_pubinei_from_web(idccpp)
        print(geoperu)
        pass