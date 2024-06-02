import requests
import json
from .models import SuSalud, IPress
from .repositories import get_susalud, insert_susalud, get_ipress, insert_ipress
from app.helpers.services import WebdriverService, convert_to_slug
from selenium.webdriver.common.by import By

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

def i_press_from_web(idipress):
    web = WebdriverService('http://app20.susalud.gob.pe:8080/registro-renipress-webapp/ipress.htm?action=mostrarVer&idipress='+idipress+'#no-back-button')
    
    # ================== FIND DATA ============================
    rows = web.getElementByPath('/html/body/div[1]/div/div[6]/div/div[1]/div[1]').find_elements(By.CLASS_NAME,"row")
    # # ================== FORMAT DATA ============================

    datos_filas = []
    for fila in rows:
        celdas = fila.find_elements(By.TAG_NAME, "div")
        datos_fila = [
            convert_to_slug(celda.text) if index == 0 else celda.text 
            for index, celda in enumerate(celdas)
        ]
        datos_filas.append(datos_fila)

    web.driver.close()

    ipress = IPress()
    ipress.key = idipress
    ipress.value = datos_filas
    return ipress
    
def get_i_press(iidipress):
    
    ipress = get_ipress(iidipress)
    
    if ipress is not None:
        return ipress
    
    ipress_from_web = i_press_from_web(iidipress)
    
    new_ipress = insert_ipress(ipress_from_web)
    
    return new_ipress