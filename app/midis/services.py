from app.helpers.services import convert_to_slug, image_to_string_array
from .repositories import get_centros_poblados, insert_centros_poblados, get_midis, insert_midis
from .models import Midis, CentrosPoblados

from app.helpers.services import WebdriverService
 
def get_data_midis_from_web(distrito, provincia, departamento, centropoblado):

    web = WebdriverService('https://public.tableau.com/views/ReporteCCPPBC/ReporteCCPP?:showVizHome=n')

    # Open district select (Click)
    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[22]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{departamento}']").click()

    web.driver.execute_script(f"document.getElementById('loadingGlassPane').remove();")

    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[23]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{provincia}']").click()

    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[24]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{distrito}']").click()

    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[25]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{centropoblado}']").click()
 
    # Find text in div (container)
    container_elements = web.getElementByPath(f"/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[33]/div/div/div/div[1]/div[5]").text.splitlines()

    # Find numbers: Screenshot to <canvas>
    web.getElementByPath(f"/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[33]/div/div/div/div[1]/div[11]/div[1]/div[2]/canvas[1]").screenshot("image.png")
 
    lines = image_to_string_array("./image.png")
    
    data = []
    for index, element in enumerate(container_elements):
        # driver.close()
        midis = Midis()
        midis.departamento = departamento
        midis.provincia = provincia
        midis.distrito = distrito
        midis.centro_poblado = centropoblado
        
        midis.key = element
        midis.value = lines[index][1]  if 0 <= index < len(lines) else ""
        data.append(midis)
        
    return data

def get_data_midis(distrito, provincia, departamento, centropoblado):
    
    midis = get_midis(distrito, provincia, departamento, centropoblado)
    
    if midis.count() != 0:
        return midis
    
    insert_midis(get_data_midis_from_web(distrito, provincia, departamento, centropoblado))
    
    return get_midis(distrito, provincia, departamento, centropoblado)
    
def get_centro_poblados_from_web(distrito, provincia, departamento, centros_poblados):
    
    URL = 'https://public.tableau.com/views/ReporteCCPPBC/ReporteCCPP?:showVizHome=n'
    
    web = WebdriverService(URL)
    
    # ================== FIND DATA ============================

    # Open district select (Click)
    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[22]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{departamento}']").click()

    web.driver.execute_script(f"document.getElementById('loadingGlassPane').remove();")

    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[23]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{provincia}']").click()

    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[24]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{distrito}']").click()
    
    web.getElementByPath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[25]/div/div/div/div/div/div/div[3]/span').click()
    web.getElementByPath(f"//*[@title='{centros_poblados}']").click()

    container_elements = web.getElementByPath(f"/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[33]/div/div/div/div[1]/div[5]").text.splitlines()
    
    centros_poblados_model = CentrosPoblados()
    centros_poblados_model.key = distrito + provincia + departamento + centros_poblados
    centros_poblados_model.value = container_elements
    return centros_poblados_model

def get_centro_poblados(distrito, provincia, departamento, centros_poblados):
        
    centro_poblado = get_centros_poblados(distrito, provincia, departamento, centros_poblados)
    
    if centro_poblado.count() != 0:
        return centro_poblado
    
    insert_centros_poblados(get_centro_poblados_from_web(distrito, provincia, departamento, centros_poblados))
    
    centro_poblado = get_centros_poblados(distrito, provincia, departamento, centros_poblados)
    
    return centro_poblado