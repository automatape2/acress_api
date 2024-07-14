from django.core.management.base import BaseCommand
from tqdm import tqdm
import pandas as pd
from app.helpers.services import convert_to_slug
import json
from app.pea2017.models import Pea2017

class Command(BaseCommand):
    help = 'Comando con barra de progreso'
    
    region = None
    province = None
    district = None
    
    array_list = []

    def handle(self, *args, **kwargs):
        
        for i in range(1, 26):
            self.region = None
            self.province = None
            self.district = None
            if i == 15:
                continue
            archivo_excel = './excels/'+f'{i:02}'+'TOMO_01.xlsx'
            print(archivo_excel)
            
            new_column_names = ["scope", "total", "14_a_29_anos", "30_a_44_anos", "45_a_64_anos", "65_y_mas_anos"]
            
            df = pd.read_excel(archivo_excel, skiprows=2, names=new_column_names)
            
            for indice, row in df.iterrows():
                
                if pd.notna(row["scope"]) :
                    if self.search_in_scope("DEPARTAMENTO", row) or self.search_in_scope("PROV.", row) :
                        self.region = row.get("scope")
                        
                    elif self.search_in_scope("PROVINCIA", row) :
                        self.province = row.get("scope")
                        
                    elif self.search_in_scope("DISTRITO", row) :
                        self.district = row.get("scope")
                        
                    elif self.search_in_scope("NO PEA",row) :
                        self.save_element("no_pea",row)
                
                    elif self.search_in_scope("PEA",row) :
                        self.save_element("pea",row)
                        
                    elif self.search_in_scope("Ocupada",row) :
                        self.save_element("pea_ocupada",row)
                        
                    elif self.search_in_scope("Desocupada",row) :
                        self.save_element("pea_desocupada",row)
                
            with open('mi_archivo.json', 'w', encoding='utf-8') as archivo:
                json.dump(self.array_list, archivo, ensure_ascii=False, indent=4)
            # print(json.dumps(self.array_list, ensure_ascii=False, indent=4))
                
    def search_in_scope(self, search, row):
        return (lambda: search in row.get("scope") )()
    
    def save_element(self, key, row):
        if self.element_exists(key, self.array_list, self.region, self.province, self.district) is None:
            pea = Pea2017()
            pea.key = key
            pea.value = row["total"]
            pea.departamento = self.region
            pea.provincia = self.province
            pea.distrito = self.district
            pea.save()
            self.array_list.append({"key": key, "value": row["total"], "departamento": self.region, "province": self.province, "district": self.district})
     
    def element_exists(self, key, lista, departamento, province, district):
        for elemento in lista:
            if (elemento["departamento"] == departamento and
                elemento["province"] == province and
                elemento["district"] == district and
                elemento["key"] == key
                ):
                return elemento
        return None