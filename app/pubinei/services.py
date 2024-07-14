from .repositories import  get_pubinei, insert_pubinei
from app.helpers.services import convert_to_slug
# from selenium.webdriver.common.by import By
from .models import Pubinei

def get_pubinei_from_web(distrito):
    web = WebdriverService('https://censos2017.inei.gob.pe/bininei2/RpWebStats.exe/CrossTab?BASE=CPV2017&ITEM=CRUZCOMBI&lang=esp')

    # Quitar seleccion
    web.getElementByPath('/html/body/div[2]/div[4]/form/div[2]/div[1]/div[1]/span').click()
    web.getElementByPath("//li[contains(text(), 'P5a+: La semana pasada, según fué su seccion, ¿A que actividad se dedicó el nego')]").click()

    # Desplegar Nivel de Manzana
    web.getElementByPath("/html/body/div[2]/div[4]/form/div[2]/div[3]/div[1]/span").click()
    web.getElementByPath("//li[contains(text(), 'Distrito')]").click()
    
    # Desplegar distrito
    web.getElementByPath("/html/body/div[2]/div[4]/form/div[3]/div[1]/div[1]/div[1]/span").click()
    web.getElementByPath("//li[contains(text(), '"+distrito+"')]").click()
    
    # Submit
    web.getElementByPath("/html/body/div[2]/div[4]/form/div[4]/input[1]").click()

    filas = web.getElementByPath("/html/body/div[2]/div[3]/div/div[1]/div/div/div[1]/table").find_elements(By.TAG_NAME, "tr")[10:20]

    datos_filas = []
    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, "td")
        datos_fila = [
            convert_to_slug(celda.text) if index == 1 else celda.text 
            for index, celda in enumerate(celdas)
        ]
        datos_filas.append(datos_fila)
    
    pubinei = Pubinei()
    pubinei.key = distrito
    pubinei.value = datos_filas
    
    return pubinei

def get_pubinei_data(distrito):
    pubinei = get_pubinei(distrito)
    
    if pubinei is not None:
        return pubinei
    
    pubinei_from_web = get_pubinei_from_web(distrito)
       
    pubinei = insert_pubinei(pubinei_from_web)
    
    return pubinei