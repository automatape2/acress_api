from app.helpers.services import convert_to_slug, image_to_string_array
from .repositories import get_idhs

def get_data_idhs(distrito, provincia, departamento):
    
    idhs = get_idhs(departamento, provincia, distrito)
    
    return idhs
     