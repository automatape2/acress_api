from .repositories import  get_pubinei, insert_pubineis
from app.helpers.services import convert_to_slug
from selenium.webdriver.common.by import By
from .models import Pubinei
from app.helpers.services import WebdriverService

def get_pubinei_from_web(departamento, provincia, distrito):
    web = WebdriverService('https://censos2017.inei.gob.pe/bininei2/RpWebStats.exe/CrossTab?BASE=CPV2017&ITEM=CRUZCOMBI&lang=esp')

    # Quitar seleccion
    web.getElementByPath('/html/body/div[2]/div[4]/form/div[2]/div[1]/div[1]/span').click()
    web.getElementByPath("//li[contains(text(), 'P5a+: La semana pasada, según fué su seccion, ¿A que actividad se dedicó el nego')]").click()

    # Desplegar Nivel de Manzana
    web.getElementByPath("/html/body/div[2]/div[4]/form/div[2]/div[3]/div[1]/span").click()
    web.getElementByPath("//li[contains(text(), 'Distrito')]").click()
    
    # Desplegar distrito
    full_ubigeo = departamento + ", " + provincia + ", distrito: " + distrito
    web.getElementByPath("/html/body/div[2]/div[4]/form/div[3]/div[1]/div[1]/div[1]/span").click()
    web.getElementByPath("//li[contains(text(), '"+full_ubigeo+"')]").click()
    
    # Submit
    web.getElementByPath("/html/body/div[2]/div[4]/form/div[4]/input[1]").click()

    filas = web.getElementByPath("/html/body/div[2]/div[3]/div/div[1]/div/div/div[1]/table").find_elements(By.TAG_NAME, "tr")[10:20]

    datos_filas = []
    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, "td")
        
        datos_fila = {}
        for index, celda in enumerate(celdas):
            
            if celda.text == " ":
                continue;
            
            if index == 1:
                datos_fila['nombre'] = celda.text
            if index == 2:
                datos_fila['casos'] = celda.text
            if index == 3:
                datos_fila['porcentaje'] = celda.text
            
        datos_filas.append(datos_fila)
    
    pubineis = []
    
    for datos_fila in datos_filas:
        pubinei = Pubinei()
        pubinei.departamento = departamento
        pubinei.provincia = provincia
        pubinei.distrito = distrito
        
        pubinei.nombre = datos_fila['nombre']
        
        casos_sin_espacios = datos_fila['casos'].replace(" ", "")
        casos_integer = int(casos_sin_espacios)
        pubinei.casos = casos_integer
        
        porcentaje_sin_simbolo = datos_fila['porcentaje'].replace("%", "")
        porcentaje_float = float(porcentaje_sin_simbolo.replace(",", "."))
        pubinei.porcentaje = porcentaje_float
        
        pubineis.append(pubinei)
    
    return pubineis

def get_pubinei_data(departamento, provincia, distrito):
    pubinei = get_pubinei(departamento, provincia, distrito)
    
    if pubinei.count() != 0:
        return pubinei
    
    insert_pubineis(
        get_pubinei_from_web(departamento, provincia, distrito)
    )
    
    pubinei = get_pubinei(departamento, provincia, distrito)
    
    
    return pubinei