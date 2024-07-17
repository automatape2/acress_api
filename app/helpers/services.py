from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import unidecode
import easyocr
import requests

class WebdriverService:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Ejecutar Chrome en modo headless (sin interfaz gráfica)
        options.add_argument('--no-sandbox')  # Solucionar problemas de permisos en algunos sistemas
        options.add_argument('--disable-dev-shm-usage')  # Usar /tmp en lugar de /dev/shm
        
        service = Service(executable_path='/usr/bin/chromedriver')
        
        self.driver = webdriver.Chrome(service=service, options=options)
        
        self.driver.get(url)
   
    def getElementByPath(self, string_path):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, f""+string_path))
        )
        

def convert_to_slug(text):
    
    text = re.sub(r'\W+', '_', 
            unidecode.unidecode(text).lower()
        ).strip('_')

    return text

def image_to_string_array(image_path):
    return easyocr.Reader(['en']).readtext(image_path)

def descargar_ubigeo_departamento():
    return requests.get('https://raw.githubusercontent.com/ernestorivero/Ubigeo-Peru/master/json/ubigeo_peru_2016_departamentos.json').json()

def descargar_ubigeo_provincia():
    return requests.get('https://raw.githubusercontent.com/ernestorivero/Ubigeo-Peru/master/json/ubigeo_peru_2016_provincias.json').json()

def descargar_ubigeo_distrito():
    return requests.get('https://raw.githubusercontent.com/ernestorivero/Ubigeo-Peru/master/json/ubigeo_peru_2016_distritos.json').json()
    
def from_departamento_to_ubigeo(departamento)-> str: 
    departamentos_ubigeo = descargar_ubigeo_departamento()
    
    ubigeo = None
    for departamento_ubigeo in departamentos_ubigeo:
        if str(departamento_ubigeo['name']).strip() == str(departamento).strip():
            ubigeo = departamento_ubigeo['id']

    return str(ubigeo)



def from_provincia_to_ubigeo(departamento_ubigeo, provincia)-> str:
    
    provincias_ubigeo = descargar_ubigeo_provincia()
    ubigeo = None
     
    for provincia_ubigeo in provincias_ubigeo:
        if str(provincia_ubigeo['name']).strip() == str(provincia).strip() and str(provincia_ubigeo['department_id']).strip() == str(departamento_ubigeo).strip():
            ubigeo = provincia_ubigeo['id']
            break

    return str(ubigeo)

 
def from_distrito_to_ubigeo(provincia_ubigeo,  distrito)-> str:

    distritos_ubigeo = descargar_ubigeo_distrito()
    ubigeo = None
    for distrito_ubigeo in distritos_ubigeo:
        if str(distrito_ubigeo['name']).strip() == str(distrito).strip() and str(distrito_ubigeo['province_id']).strip() == str(provincia_ubigeo).strip():
            ubigeo = distrito_ubigeo['id']
    
    return str(ubigeo)


# def getElementByPath(driver, string_path):
#     return WebDriverWait(driver, 30).until(
#         EC.visibility_of_element_located((By.XPATH, f""+string_path))
#     )

 