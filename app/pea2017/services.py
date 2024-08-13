from .repositories import  get_pea2017, insert_pea
from .models import Pea2017
# import pandas as pd
# from pandas.core.frame import DataFrame

def get_pea2017_data(departamento: str, provincia: str, distrito: str):
    pea2017 = get_pea2017(departamento, provincia, distrito)
    return pea2017

# def upload_pea(filepath: str):
#     excel = pd.read_excel(filepath)
#     pea = load_pea_from_excel(excel)
#     insert_pea(pea)

#     return pea

# def load_pea_from_excel(excel_file: DataFrame):
#     region = excel_file.iloc[3,0]
#     code = region.split()[-1]
#     occupied_pea = excel_file.iloc[13,1]
#     unoccupied_pea = excel_file.iloc[18,1]
#     no_pea = excel_file.iloc[23,1]
    
#     pea = Pea2017()
#     pea.codigo = code
#     pea.departamento = region
#     pea.pea_ocupada = occupied_pea
#     pea.pea_desocupada = unoccupied_pea
#     pea.no_pea = no_pea
    
#     return pea