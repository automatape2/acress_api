from app.helpers.services import convert_to_slug, image_to_string_array
from .repositories import get_nbis

def get_data_nbis(distrito, provincia, departamento):
    
    nbis = get_nbis(departamento, provincia, distrito)
    
    return nbis
     