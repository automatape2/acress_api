from django.shortcuts import render
from django.http import JsonResponse
from .models import Pubinei

def index(request):
    if request.method == 'GET':
        mymodels = Pubinei.objects.all()
        data = list(mymodels.values())  # Convierte el queryset a una lista de diccionarios
        return JsonResponse(data, safe=False)