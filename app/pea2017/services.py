from .repositories import  get_pea2017, insert_pea
from .models import Pea2017
import pandas as pd

def get_pea2017_data(departamento):
    pea2017 = get_pea2017(departamento)
    return pea2017

def upload_pea(filepath):
    excel = pd.read_excel(filepath)

    pea = load_pea_from_excel(excel)

    insert_pea(pea)

    return pea

def load_pea_from_excel(excel_file):
    departamento = excel_file.iloc[3,0]
    codigo = departamento.split()[-1]
    pea_ocupada = excel_file.iloc[13,1]
    pea_desocupada = excel_file.iloc[18,1]
    no_pea = excel_file.iloc[23,1]
    
    pea = Pea2017()
    pea.codigo = codigo
    pea.departamento = departamento
    pea.pea_ocupada = pea_ocupada
    pea.pea_desocupada = pea_desocupada
    pea.no_pea = no_pea
    
    return pea