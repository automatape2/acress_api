from django.core.management.base import BaseCommand
from app.geoperu.services import get_pubinei_from_web
from app.helpers.services import descargar_ubigeo_distrito
from app.geoperu.models import GeoPeru
from tqdm import tqdm

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        distritos_ubigeo = descargar_ubigeo_distrito()

        barra_progreso = tqdm(
            total=len(distritos_ubigeo),
        )

        for distrito in distritos_ubigeo:
            for index in list(range(300)):
                codigo_centro_poblado = distrito["id"] + str(index + 1).zfill(4)
                
                script = GeoPeru.objects.filter(idccpp=codigo_centro_poblado)
                if script.exists():
                    if script.count() >= 24:
                        break
                    
                geoperus = get_pubinei_from_web(codigo_centro_poblado)

                barra_progreso.set_description(codigo_centro_poblado)

                if geoperus is None:
                    break

                for geoperu in geoperus:
                    if GeoPeru.objects.filter(idccpp=geoperu.idccpp, indicador=geoperu.indicador).exists():
                        continue
                    geoperu.save()

            barra_progreso.update(1)