from django.core.management.base import BaseCommand
from app.midis.services import get_data_midis_from_web
from app.helpers.services import descargar_ubigeo_distrito, descargar_ubigeo_departamento, descargar_ubigeo_provincia
from app.midis.models import Midis
from tqdm import tqdm

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        departamentos_ubigeo = descargar_ubigeo_departamento()
        provincias_ubigeo = descargar_ubigeo_provincia()
        distritos_ubigeo = descargar_ubigeo_distrito()

        barra_progreso = tqdm(
            total=len(distritos_ubigeo),
        )

        

        for departamento in departamentos_ubigeo:

            barra_progreso.set_description(f"Departamento: {departamento['name']}")

            for provincia in provincias_ubigeo:

                if provincia['department_id'] != departamento['id']:
                    continue

                for distrito in distritos_ubigeo:

                    if not Midis.objects.filter(
                        distrito=midis.distrito
                    ).exists():
                        continue
                    if distrito['province_id'] != provincia['id']:
                        continue
                 
                    for i in range(200):
                        try:
                            midises = get_data_midis_from_web(
                                distrito['name'],
                                provincia['name'],
                                departamento['name'],
                                distrito['id'] + str(i+1).zfill(4)
                            )

                            for midis in midises:
                                midis.save()
                        except Exception as e:
                            print(e)
                            break
                                
                  
                    barra_progreso.update(1)
                        
