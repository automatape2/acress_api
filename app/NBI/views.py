from django.http import JsonResponse
from django.shortcuts import render
from .services import get_data_nbis

def index(request):
    departamento = request.GET.get('departamento', default="Lima")
    provincia = request.GET.get('provincia', default="Lima")
    distrito = request.GET.get('distrito', default="Lima")

    nbis = get_data_nbis(distrito, provincia, departamento)
    
    response = [
        {
            "tipo": nbi.tipo,
            "casos": nbi.casos,
            "porcentaje": nbi.porcentaje,
        }
        for nbi in nbis
    ]
    return JsonResponse(response, safe=False)
