from django.core.management.base import BaseCommand
from tqdm import tqdm
import pandas as pd
from app.helpers.services import convert_to_slug
import json
from app.NBI.models import NBI

class Command(BaseCommand):
    help = 'Comando con barra de progreso'
    
    region = None
    province = None
    district = None
    
    array_list = []

    def handle(self, *args, **kwargs):
        
        archivo_excel = './excels/NBI POR TIPO DE CARENCIA, NIVEL DISTRITAL.xlsx'
        
        # new_column_names = ["scope", "total", "14_a_29_anos", "30_a_44_anos", "45_a_64_anos", "65_y_mas_anos"]
        
        df = pd.read_excel(archivo_excel, skiprows=8)
        
        
        # bucle para recorrer las filas
        # data = []
        for index, row in tqdm(df.iterrows(), total=df.shape[0]):
            if pd.isna(row[2]) :
                continue
            
            departamento = row[2]
            provincia = row[3]
            distrito = row[4]
            
            vivienda_con_caracteristicas_fisicas = row[6]
            vivienda_con_caracteristicas_fisicas_porcentaje = row[7]
            vivienda_con_hacinamiento = row[8]
            vivienda_con_hacinamiento_porcentaje = row[9]
            vivienda_sin_servicios_higienicos = row[10]
            vivienda_sin_servicios_higienicos_porcentaje = row[11]
            hogares_con_ninos_sin_escuela = row[12]
            hogares_con_ninos_sin_escuela_porcentaje = row[13]
            hogares_con_alta_dependencia_economica = row[14]
            hogares_con_alta_dependencia_economica_porcentaje = row[15]
            
            
            for i in range(4):
                if i == 0:
                    tipo = "Viviendas con características físicas inadecuadas"
                    casos = vivienda_con_caracteristicas_fisicas
                    porcentaje = vivienda_con_caracteristicas_fisicas_porcentaje
                elif i == 1:
                    tipo = "Viviendas con hacinamiento"
                    casos = vivienda_con_hacinamiento
                    porcentaje = vivienda_con_hacinamiento_porcentaje
                elif i == 2:
                    tipo = "Viviendas sin servicios higiénicos"
                    casos = vivienda_sin_servicios_higienicos
                    porcentaje = vivienda_sin_servicios_higienicos_porcentaje
                elif i == 3:
                    tipo = "Hogares con niños sin acceso a educación"
                    casos = hogares_con_ninos_sin_escuela
                    porcentaje = hogares_con_ninos_sin_escuela_porcentaje
                elif i == 4:
                    tipo = "Hogares con alta dependencia económica"
                    casos = hogares_con_alta_dependencia_economica
                    porcentaje = hogares_con_alta_dependencia_economica_porcentaje
            
                nbi_model = NBI()
                nbi_model.departamento = departamento
                nbi_model.provincia = provincia
                nbi_model.distrito = distrito
                nbi_model.tipo = tipo
                nbi_model.casos = casos
                nbi_model.porcentaje = porcentaje
                nbi_model.save()
                # data.append(nbi_}model)
             
                
    def search_in_scope(self, search, row):
        return (lambda: search in row.get("scope") )()
     