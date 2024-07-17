from django.http import JsonResponse
from django.shortcuts import render
from .services import get_data_minedu

def index(request):
    departamento = request.GET.get('departamento', default="Lima")
    provincia = request.GET.get('provincia', default="Lima")
    distrito = request.GET.get('distrito', default="Lima")

    minedus = get_data_minedu(departamento, provincia, distrito)
    
    total = 0
    
    for minedu in minedus:
        for nivel in minedu.niveles:
            total += int(nivel["estudiantes"])
    
    response = [
    {
        "localidad": distrito,
        "total": total,
        "colegios": [
            {
                "nombre": minedu.nombre,
                "niveles": minedu.niveles
            }
            for minedu in minedus
        ]
    }
]
 
    return JsonResponse(response, safe=False)
