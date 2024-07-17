from django.http import JsonResponse
from django.shortcuts import render
from .services import get_data_idhs

def index(request):
    departamento = request.GET.get('departamento', default="Lima")
    provincia = request.GET.get('provincia', default="Lima")
    distrito = request.GET.get('distrito', default="Independencia")

    idhs = get_data_idhs(distrito, provincia, departamento)
    
    response = [
        {
            "nombre": idh.key,
            "detalle": idh.detalle,
            "rank": idh.ranking
        } 
        for idh in idhs
    ]
    return JsonResponse(response, safe=False)
