from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_pea2017_data
from django.conf import settings
import os
from django.core import serializers

def index(request):
    if request.method == 'GET':
        departamento = request.GET.get('departamento', default="DEPARTAMENTO TACNA")
        provincia = request.GET.get('provincia', default="PROVINCIA TACNA")
        distrito = request.GET.get('distrito', default="DISTRITO TACNA")
    
        peas2017 = get_pea2017_data(departamento,provincia,distrito)
        
        # if pea2017 is None:
        #     return JsonResponse([{"message":"Ese departamento no tiene resulados"}], safe=False)
        
        total_pea = sum(float(pea2017.value) for pea2017 in peas2017 if pea2017.key == "pea")
        total_pea_ocupada = sum(float(pea2017.value) for pea2017 in peas2017 if pea2017.key == "pea_ocupada")
        total_pea_desocupada = sum(float(pea2017.value) for pea2017 in peas2017 if pea2017.key == "pea_desocupada")
        total_no_pea = sum(float(pea2017.value) for pea2017 in peas2017 if pea2017.key == "no_pea")
        
        return JsonResponse({
            "peaDistrito": {
                "totalPersonas": total_pea + total_no_pea,
                "totalPea": total_pea + total_no_pea,
                "pea": total_pea,
                "peaPorcentaje": total_pea / (total_pea + total_no_pea),
                "noPea": total_no_pea,
                "noPeaPorcentaje": total_no_pea / (total_pea + total_no_pea)
            },
           "peaDetalle": {
                "totalPea": total_pea,
                "peaOcupada": total_pea_ocupada,
                "peaOcupadaPorcentaje": total_pea_ocupada / (total_pea_desocupada + total_pea_ocupada),
                "peaDesOcupada": total_pea_desocupada,
                "peaDesOcupadaPorcentaje": total_pea_desocupada / (total_pea_desocupada + total_pea_ocupada),
            }
        }, safe=False)
        
        # return JsonResponse({
        #     "key": pea2017.key, 
        #     "value": pea2017.value,
        # }, safe=False)

@csrf_exempt
def pea_upload(request):
   
    if request.method == 'POST':
        request_file = request.FILES.get('file')
        
        filepath = os.path.join(settings.MEDIA_ROOT, 'uploads', request_file.name)
        
        with open(filepath, 'wb+') as destination:
            for chunk in request_file.chunks():
                destination.write(chunk)
        
        # pea = upload_pea(filepath)
        
        data = {
            "message":"File uploaded successfully",
            "data": {
                "departamento":pea.departamento,
                "pea_ocupada": pea.pea_ocupada, 
                "pea_desocupada": pea.pea_desocupada,
                "no_pea":pea.no_pea
            }
        }
        return JsonResponse(data,safe=False)
    
    return JsonResponse({
        "message": "Metodo no permitido",
        "code": 500
    },safe=False)