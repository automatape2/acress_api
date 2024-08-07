from django.http import JsonResponse
from .services import get_geoperu_data

def index(request):
    if request.method == 'GET':
        
        idccpp = request.GET.get('idccpp', default="101010002")
        
        geoperu = get_geoperu_data(idccpp)
        print(geoperu)
      
        response = {
            "total": 710,
            "lenguas": [
                {
                    "total": "Castellano",
                    "casos": 340,
                    "porcentaje": 25.00
                },
                {
                    "total": "Quechua",
                    "casos": 280,
                    "porcentaje": 75.00
                },
                {
                    "total": "Aimara",
                    "casos": 40,
                    "porcentaje": 0
                },
                {
                    "total": "Otros",
                    "casos": 30,
                    "porcentaje": 0
                },
                {
                    "total": "NS / NR",
                    "casos": 10,
                    "porcentaje": 0
                }
            ]
        }
 
        return JsonResponse(response,safe=False)
     