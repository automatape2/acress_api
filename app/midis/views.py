from django.http import JsonResponse
from .services import get_centro_poblados, get_data_midis

def index(request):
    departamento = request.GET.get('departamento', default="Lima").upper()
    provincia = request.GET.get('provincia', default="Lima").upper()
    distrito = request.GET.get('distrito', default="Lima").upper()
    centropoblado = request.GET.get('centropoblado', default="1501010001-LIMA").upper()

    midis = get_data_midis(distrito, provincia, departamento, centropoblado).value;
    return JsonResponse(midis, safe=False)

def centros_poblados(request):
    departamento = request.GET.get('departamento', default="Lima").upper()
    provincia = request.GET.get('provincia', default="Lima").upper()
    distrito = request.GET.get('distrito', default="Lima").upper()
 
    # new filter, TODO: implement does not work if you do not add
    centro_poblado_request = request.GET.get('centros_poblado', default="1501010001-Lima").upper()
   
    centros_poblados = get_centro_poblados(distrito, provincia, departamento, centro_poblado_request).value
    
    return JsonResponse(centros_poblados, safe=False)