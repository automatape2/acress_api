from .repositories import get_geoperu
from app.helpers.services import WebdriverService
  
def get_pubinei_from_web(idccpp):
    url = 'https://visor.geoperu.gob.pe/reportes/consulta_ccpp.phtml?olayer=peru_ccpp_mayor&ocampo=cod_ccpp&ovalor='+str(idccpp)
    print(url)
    web = WebdriverService(url)

    
    web.getElementByPath('/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/h1/table/tbody/tr/td').click()
    text = web.getElementByPath('/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[4]').text
    
    if text.replace(" ","") == "":
        return None
    else:
        return text    
    # web.getElementByPath("//li[contains(text(), 'P5a+: La semana pasada, según fué su seccion, ¿A que actividad se dedicó el nego')]").click()

    # # Desplegar Nivel de Manzana
    # web.getElementByPath("/html/body/div[2]/div[4]/form/div[2]/div[3]/div[1]/span").click()
    # web.getElementByPath("//li[contains(text(), 'Distrito')]").click()
     
def get_geoperu_data(idccpp):
    return get_pubinei_from_web(idccpp=idccpp)
    # return get_geoperu(departamento, provincia, distrito, idccpp)