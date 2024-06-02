from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import unidecode
import easyocr

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


def getElementByPath(driver, string_path):
    return WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, f""+string_path))
    )
 