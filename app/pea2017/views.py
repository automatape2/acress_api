from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_pea2017_data, upload_pea
from django.conf import settings
import os

def index(request):
    if request.method == 'GET':
        departamento = request.GET.get('departamento', default="AMAZONAS")
    
        pea2017 = get_pea2017_data(departamento)
        
        if pea2017 is None:
            return JsonResponse([{"message":"Ese departamento no tiene resulados"}], safe=False)
        
        return JsonResponse({
            "departamento":pea2017.departamento,
            "pea_ocupada": pea2017.pea_ocupada, 
            "pea_desocupada": pea2017.pea_desocupada,
            "no_pea":pea2017.no_pea
        }, safe=False)

@csrf_exempt
def pea_upload(request):
   
    if request.method == 'POST':
        request_file = request.FILES.get('file')
        
        filepath = os.path.join(settings.MEDIA_ROOT, 'uploads', request_file.name)
        
        with open(filepath, 'wb+') as destination:
            for chunk in request_file.chunks():
                destination.write(chunk)
        
        pea = upload_pea(filepath)
        
        data = {
            "message":"Archivo subido exitosamente",
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