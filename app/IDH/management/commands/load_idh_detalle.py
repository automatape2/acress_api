from django.core.management.base import BaseCommand
from tqdm import tqdm
from app.pubinei.models import Pubinei, Poblacion
import pandas as pd
from app.helpers.services import convert_to_slug
import json
from app.IDH.models import IDH

class Command(BaseCommand):
    help = 'Comando con barra de progreso'
    
    region = None
    province = None
    district = None
    
    array_list = []

    def handle(self, *args, **kwargs):
        
        archivo_excel = './excels/IDH 2019.xlsx'
        
        df = pd.read_excel(archivo_excel, skiprows=2, sheet_name="Distrital")
        column_names = df.columns
        print(df.head())
        
        for index1, row in df.iterrows():
            idhs = IDH.objects.filter(ubigeo=row["UBIGEO"]).all()
            if(row[2] == "Distrito") :
                fila_nombre_detalles = row
            for idh in idhs:
                for index, col in enumerate(column_names):
                    if col == idh.key:  
                        idh.detalle = {
                            "nombre": fila_nombre_detalles[index],
                            "valor": row[index]
                        }
                        print(row["UBIGEO"],index)
                        idh.ranking = row[index+1]
                        idh.save()
                    
                
        pass
         
