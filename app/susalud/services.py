import requests
import json
from .models import SuSalud, IPress
from .repositories import get_susalud, insert_susalud, get_ipresses, insert_ipresses
from app.helpers.services import from_departamento_to_ubigeo, from_provincia_to_ubigeo, from_distrito_to_ubigeo
from selenium.webdriver.common.by import By
from app.helpers.services import WebdriverService

def get_establishment_from_web(distrito, provincia, departamento):
    url = 'http://app20.susalud.gob.pe:8080/registro-renipress-webapp/listadoEstablecimientosRegistrados.htm?action=cargarEstablecimientos&txt_filtrar=&cmb_estado=1&cmb_departamento='+departamento+'&cmb_provincia='+provincia+'&cmb_distrito='+distrito+'&cmb_institucion=0&cmb_tipo_establecimiento=0&cmb_clasificacion=0&cmb_categoria=0&cmb_unidadEjecutora=0&cmb_servicio=0&cmb_autoridadSanitaria=0&cmb_red=0&cmb_microRed=0&cmb_clas=0&cmb_colegio=0&cmb_especialidad=0&cmb_quintil=0&cmb_telesalud=0&dat_fd_quintil=&ra_reg=on&dat_fd_desde=&dat_fd_hasta='
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text.replace("\"draw\":,", "\"draw\":\"\",")
        susalud  = SuSalud()
        susalud.key = distrito + provincia + departamento
        susalud.value = json.loads(data)
        return susalud
    else:
        return None
        
def get_establecimientos(distrito, provincia, departamento):
    
    su_salud = get_susalud(distrito, provincia, departamento)
    
    if su_salud is not None:
        return su_salud
    
    su_salud_from_web = get_establishment_from_web(distrito, provincia, departamento)
    
    new_susalud = insert_susalud(su_salud_from_web)
    
    return new_susalud

def i_press_from_web(departamento, provincia, distrito):
    ipresses = []
    
    departamento_ubigeo = from_departamento_to_ubigeo(departamento)[-2:]
    provincia_ubigeo = from_provincia_to_ubigeo(departamento_ubigeo, provincia)[-2:]
    distrito_ubigeo = from_distrito_to_ubigeo(departamento_ubigeo+provincia_ubigeo, distrito)[-2:]
    
    
    url = 'http://app20.susalud.gob.pe:8080/registro-renipress-webapp/listadoEstablecimientosRegistrados.htm?action=cargarEstablecimientos&txt_filtrar=&cmb_estado=1&cmb_departamento='+str(departamento_ubigeo)+'&cmb_provincia='+str(provincia_ubigeo)+'&cmb_distrito='+str(distrito_ubigeo)+'&cmb_institucion=0&cmb_tipo_establecimiento=0&cmb_clasificacion=0&cmb_categoria=0&cmb_unidadEjecutora=0&cmb_servicio=0&cmb_autoridadSanitaria=0&cmb_red=0&cmb_microRed=0&cmb_clas=0&cmb_colegio=0&cmb_especialidad=0&cmb_quintil=0&cmb_telesalud=0&dat_fd_quintil=&ra_reg=on&dat_fd_desde=&dat_fd_hasta='
    
    response = requests.get(url)
    
    response_json = json.loads(response.text.replace("\"draw\":,", "\"draw\":\"\","))
    
    items = response_json.get('data', [])
    
    for item in items:
        idipress = item["codigounico"]
        # print('http://app20.susalud.gob.pe:8080/registro-renipress-webapp/ipress.htm?action=mostrarVer&idipress='+idipress+'#no-back-button')
        web = WebdriverService('http://app20.susalud.gob.pe:8080/registro-renipress-webapp/ipress.htm?action=mostrarVer&idipress='+idipress+'#no-back-button')
        
        # ================== FIND DATA ============================
        rows1 = web.getElementByPath('/html/body/div[1]/div/div[6]/div/div[1]/div[1]').find_elements(By.CLASS_NAME,"row")
        # # ================== FORMAT DATA ============================
        
        rows2 = web.getElementByPath('/html/body/div[1]/div/div[6]/div').find_elements(By.CLASS_NAME,"row")
        
        rows = rows1 + rows2
        

        datos_filas = []
        for fila in rows:
            celdas = fila.find_elements(By.TAG_NAME, "div")
            datos_fila = [ celda.text for celda in celdas ]
            datos_filas.append(datos_fila)

        web.driver.close()
        
        
        for fila in datos_filas:
            if len(fila) == 1:
                continue
            
            if fila[1] == "":
                continue
                
            ipress = IPress()
            ipress.departamento = departamento
            ipress.provincia = provincia
            ipress.distrito = distrito
            ipress.key = fila[0]
            ipress.value = fila[1].replace('"', '')
            
            ipresses.append(ipress)
        return ipresses    
    return ipresses
    
def get_i_presses(departamento, provincia, distrito):
    
    ipresses = get_ipresses(departamento, provincia, distrito)
    
    if ipresses.count() != 0:
        return ipresses
    
    insert_ipresses(i_press_from_web(departamento, provincia, distrito))
    
    return get_ipresses(departamento, provincia, distrito)