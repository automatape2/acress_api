from django.core.management.base import BaseCommand
from tqdm import tqdm
from app.pubinei.models import Pubinei, Poblacion
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
        
        archivo_excel = './excels/pubinei/12. Huancayo.xlsx'
        
        df = pd.read_excel(archivo_excel, skiprows=2)
        column_names = df.columns
        print(df.head())
        pass
        # for index, row in df.iterrows():
        #     print(row)
        #     departamento = row["DEPARTAMENTO"]
        #     provincia = row["PROVINCIA"]
        #     distrito = row["DISTRITO"]
            
        #     for col in column_names:
        #         poblacion = Poblacion()
        #         poblacion.departamento = departamento
        #         poblacion.provincia = provincia
        #         poblacion.distrito = distrito
                
        #         poblacion.key = col
        #         poblacion.value = row[col]
                
        #         poblacion.save()
