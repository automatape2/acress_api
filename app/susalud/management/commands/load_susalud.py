from django.core.management.base import BaseCommand
from app.susalud.services import get_i_presses
from app.helpers.services import descargar_ubigeo_departamento, descargar_ubigeo_provincia, descargar_ubigeo_distrito
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Comando con barra de progreso'
    departamentos = []
    provincias = []
    distritos = []
    
    def __init__(self):
        self.departamentos = descargar_ubigeo_departamento()
        self.provincias = descargar_ubigeo_provincia()
        self.distritos = descargar_ubigeo_distrito()
        
    def obtener_provincias_por_departamento_ubigeo(self, departamento_ubigeo):
        return [provincia for provincia in self.provincias if provincia['department_id'] == departamento_ubigeo]
    
    def obtener_distritos_por_provinicia_ubigeo(self, provincia_ubigeo):
        return [distrito for distrito in self.distritos if distrito['province_id'] == provincia_ubigeo]
    
    def handle(self, *args, **kwargs):
        progress = tqdm(total=len(self.distritos), desc="Progreso total")
        for departamento in self.departamentos:
            departamento_ubigeo = departamento['id']
            provincias = self.obtener_provincias_por_departamento_ubigeo(departamento_ubigeo)
            for provincia in provincias:
                provincia_ubigeo = provincia['id']
                distritos = self.obtener_distritos_por_provinicia_ubigeo(provincia_ubigeo)
                for distrito in distritos:
                    progress.set_description_str(departamento['name'] + ' ' + provincia['name'] + ' ' + distrito['name'])
                    get_i_presses(departamento['name'], provincia['name'], distrito['name'])
                    progress.update(1)
                    
     