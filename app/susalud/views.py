from django.http import JsonResponse
from .services import get_i_press, get_establecimientos

def ipress(request):
    idipress = request.GET.get('idipress', default="00005053")
    i_press = get_i_press(idipress).value
    return JsonResponse(i_press, safe=False)


def establecimientos(request):
    departamento = request.GET.get('departamento', default="01")
    provincia = request.GET.get('provincia', default="02")
    distrito = request.GET.get('distrito', default="02")
    
    establecimientos = get_establecimientos(distrito, provincia, departamento).value
    
    return JsonResponse(establecimientos, safe=False)