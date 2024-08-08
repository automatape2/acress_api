from .repositories import get_geoperu
from .models import GeoPeru
from app.helpers.services import WebdriverService
from selenium.webdriver.common.by import By

DEPLEGABLE_UBICACIONGEOGRAFICA_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/h1/table/tbody/tr/td'
DEPARTAMENTO_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[4]'
PROVINCIA_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[4]'
DISTRITO_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[4]'
CENTRO_POBLADO_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[4]'

DEPLEGABLE_DATOSDEPOBLACION_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[3]/tbody/tr/td/div/h1/table/tbody/tr/td'
TABLA_DATOSDEPOBLACION_XPATH = '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[3]/tbody/tr/td/div/div/table/tbody'
 
  
def get_pubinei_from_web(idccpp):
    url = 'https://visor.geoperu.gob.pe/reportes/consulta_ccpp.phtml?olayer=peru_ccpp_mayor&ocampo=cod_ccpp&ovalor='+str(idccpp)
    print(url)
    web = WebdriverService(url)

    web.getElementByPath(DEPLEGABLE_UBICACIONGEOGRAFICA_XPATH).click()
    centro_poblado = web.getElementByPath(CENTRO_POBLADO_XPATH).text.strip()

    if centro_poblado == "":
        return None

    web.getElementByPath(DEPLEGABLE_DATOSDEPOBLACION_XPATH).click()
    datos_poblacion_filas = web.getElementByPath(TABLA_DATOSDEPOBLACION_XPATH).find_elements(By.TAG_NAME, "tr") #Indicadores, Población, Porcentaje (%)

    for fila in datos_poblacion_filas:
        celdas = fila.find_elements(By.TAG_NAME, "td")

        indicador = None
        poblacion = None
        porcentaje = None

        for index, celda in enumerate(celdas):
            if index == 0:
                indicador = celda.text
            if index == 1:
                poblacion = celda.text
            if index == 2:
                porcentaje = celda.text

        return GeoPeru(
            idccpp=idccpp,
            indicador=indicador,
            poblacion=poblacion,
            porcentaje=porcentaje
        )

     
def get_geoperu_data(idccpp):
    return get_pubinei_from_web(idccpp=idccpp)
