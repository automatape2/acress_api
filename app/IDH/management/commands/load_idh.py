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
        
        df = pd.read_excel(archivo_excel, skiprows=3)
        column_names = df.columns
        print(column_names, df.head(50))
        # pass
        departamento = None
        provincia = None
        distrito = None
        ubigeo = None
        for index, row in df.iterrows():
            if pd.isna(row["UBIGEO"]) :
                continue
            
            
            if pd.notna(row["DEPARTAMENTO"]) and not str(row["DEPARTAMENTO"]).isdigit():
                departamento = row["DEPARTAMENTO"]
        
            if pd.isna(row["DEPARTAMENTO"]) and pd.notna(row[2]):
                provincia = row[2]
                
            if str(row["DEPARTAMENTO"]).isdigit() and pd.notna(row[2]):
                distrito = row[2]
                
            ubigeo = row["UBIGEO"]
            # print(departamento, provincia, distrito)
            if departamento != None and provincia != None and distrito != None: 
                for index, col in enumerate(column_names):
                    if index <= 4:
                        continue
                    if col == "Unnamed: 10" or col == "Unnamed: 2" or col == "Unnamed: 3" or col == "Unnamed: 4": 
                        continue
                    
                    idh = IDH()
                    idh.departamento = departamento.strip()
                    idh.provincia = provincia.strip()
                    idh.distrito = distrito.strip()
                    idh.ubigeo = ubigeo.strip()
                    
                    if col == "Unnamed: 16":
                        idh.key = "Índice de desarrollo Humano (IDH)"    
                    else:
                        idh.key = col
                        
                    idh.value = row[col]
                    
                    idh.save()
        
        pass
         
