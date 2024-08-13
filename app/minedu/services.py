from app.helpers.services import from_departamento_to_ubigeo, from_provincia_to_ubigeo, from_distrito_to_ubigeo
from .repositories import get_minedu, insert_minedu
from .models import Minedu
from selenium.webdriver.common.by import By
import requests
import json
from itertools import groupby
from operator import itemgetter

from app.helpers.services import WebdriverService
 
def get_data_minedu_from_web(distrito, provincia, departamento):

    # web = WebdriverService('https://escale.minedu.gob.pe/web/inicio/padron-de-iiee')
    
    departamento_ubigeo = from_departamento_to_ubigeo(departamento)
    provincia_ubigeo = from_provincia_to_ubigeo(departamento_ubigeo, provincia)
    distrito_ubigeo = from_distrito_to_ubigeo(provincia_ubigeo, distrito)

    url = 'https://escale.minedu.gob.pe/padron/rest/instituciones?estados=1&ubigeo='+str(distrito_ubigeo)
    print(url)
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        
        items = response.json().get('items', [])
        
        items_sorted = sorted(items, key=itemgetter('codinst'))
        items_grouped = groupby(items_sorted, key=itemgetter('codinst'))
        items_grouped2 = groupby(items_sorted, key=itemgetter('codinst'))
        
         
        
            
        total = 0
        for key, group2 in items_grouped2:
            for item2 in group2:
                try:
                    total += int(item2["estadistica"]["talumno"])
                except KeyError:
                    pass
                
        minedus = []
        if total != 0:
            for key, group in items_grouped:
            
                minedu  = Minedu()
                minedu.departamento = departamento
                minedu.provincia = provincia
                minedu.distrito = distrito
                
                niveles = []
                for item in group:
                    nombre = item["cenEdu"]
                    
                    try:
                        nivel = item["estadistica"]["nivelModalidad"]["valor"]
                        estudiantes = int(item["estadistica"]["talumno"])
                        porcentaje = round( float(item["estadistica"]["talumno"]) / total * 100, 2 )
                    except:
                        nivel = ""
                        estudiantes = 0
                        porcentaje = 0
                        
                    niveles.append({
                            "nivel": nivel,
                            "estudiantes": estudiantes,
                            "porcentaje": porcentaje
                        })
                        
                minedu.nombre = nombre
                minedu.niveles = niveles
                
                minedus.append(minedu)
         
        return minedus
    

def get_data_minedu(departamento, provincia, distrito):
    
    minedus = get_minedu(departamento, provincia, distrito)
    
    if minedus.count() != 0:
        return minedus
    
    insert_minedu(get_data_minedu_from_web(distrito, provincia, departamento))
    
    return get_minedu(departamento, provincia, distrito)
    