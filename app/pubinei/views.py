from django.shortcuts import render
from django.http import JsonResponse
from .services import get_pubinei_data

def peaCP(request):
    if request.method == 'GET':
        
        departament = request.GET.get('departamento', default="Huancavelica")
        province = request.GET.get('provincia', default="Huancavelica")
        district = request.GET.get('distrito', default="Pilchaca")
        
        pubineis = get_pubinei_data(departament, province, district)
      
        response = {
            "total: ": pubineis.count(),
            "detalles": [
                pubinei.to_dict() for pubinei in pubineis
            ]
        }
        
        return JsonResponse(response,safe=False)
    
def index(request):
    if request.method == "GET":
        departamento = request.GET.get('departamento', default="Lima")
        provincia = request.GET.get('provincia', default="Lima")
        distrito = request.GET.get('distrito', default="Lima")
        
        
        