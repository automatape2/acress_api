from django.shortcuts import render
from django.http import JsonResponse
from .services import get_pubinei_data
import json

def index(request):
    if request.method == 'GET':
        # Get from request the values of the parameters departamento, provincia and distrito
        departament = request.GET.get('departamento', default="Huancavelica")
        province = request.GET.get('provincia', default="Huancavelica")
        district_request = request.GET.get('distrito', default="Pilchaca")
        district = request.GET.get('distrito', default=departament+", "+province+", distrito: "+district_request)
        
        # Get all the data from web or cache (database)
        pubinei = get_pubinei_data(district).value
        
        # Return the data in JSON format 
        return JsonResponse(pubinei,safe=False)
        