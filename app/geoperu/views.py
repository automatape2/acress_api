from django.http import JsonResponse
from .services import get_geoperu_data

def index(request):
    if request.method == 'GET':
        
        idccpp = request.GET.get('idccpp', default="101010001")
        
        geoperus = get_geoperu_data(idccpp)
        
        response = {
            "total": sum(int(geoperu.poblacion.replace(",","")) for geoperu in geoperus),
            "lenguas": [
                {
                    "total": geoperu.indicador,
                    "casos": int(geoperu.poblacion.replace(",","")),
                    "porcentaje": round(float(geoperu.porcentaje),2)
                }
                for geoperu in geoperus        
            ]
        }
 
        return JsonResponse(response,safe=False)
     