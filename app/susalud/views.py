from django.http import JsonResponse
from .services import get_i_presses, get_establecimientos

def ipress(request):
    # 00005053
    departamento = request.GET.get('departamento', default="Lima")
    provincia = request.GET.get('provincia', default="Lima")
    distrito = request.GET.get('distrito', default="Lima")
    
    i_presses = get_i_presses(departamento, provincia, distrito)
    
    response = [
        {
            "nombre": i_presses.filter(key__icontains='Razón Social').first().value,
            "ubicacion": i_presses.filter(key__icontains='Departamento').first().value+
                " – "+
                i_presses.filter(key__icontains='Provincia').first().value
                +" – "+
                i_presses.filter(key__icontains='Distrito').first().value,
            "representante": i_presses.filter(key__icontains='Representante').first().value,
            
            "codigo": {
                "name": i_presses.filter(key__icontains='IPRESS').first().key,
                "value": i_presses.filter(key__icontains='IPRESS').first().value
            },
            "categoria": {
                "name": i_presses.filter(key__icontains='Categoría').first().key,
                "value": i_presses.filter(key__icontains='Categoría').first().value
            },
            "tipo": {
               "name": i_presses.filter(key__icontains='Tipo de Establecimiento').first().key,
                "value": i_presses.filter(key__icontains='Tipo de Establecimiento').first().value
            },
            "subcategoría": {
              "name": i_presses.filter(key__icontains='Clasificación').first().key,
                "value": i_presses.filter(key__icontains='Clasificación').first().value.split('\n')[7] if len(i_presses.filter(key__icontains='Clasificación').first().value.split('\n')) >= 8 else "La línea no existe"
            },
            "estado": {
               "name": i_presses.filter(key__icontains='Estado').first().key,
                "value": i_presses.filter(key__icontains='Estado').first().value
            },
            "condicion": {
              "name": i_presses.filter(key__icontains='Condición').first().key,
                "value": i_presses.filter(key__icontains='Condición').first().value
            },
            "diresa": {
               "name": i_presses.filter(key__icontains='DIRESA').first().key,
                "value": i_presses.filter(key__icontains='DIRESA').first().value
            },
            "red": {
              "name": i_presses.filter(key__icontains='RED').first().key,
                "value": i_presses.filter(key__icontains='RED').first().value
            },
            "microred": {
             "name": i_presses.filter(key__icontains='MICRORED').first().key,
                "value": i_presses.filter(key__icontains='MICRORED').first().value
            },
            "establecimiento": {
             "name": i_presses.filter(key__icontains='Tipo de Establecimiento').first().key,
                "value": i_presses.filter(key__icontains='Tipo de Establecimiento').first().value
            },
            # "establecimiento_telefono": {
            #    "name": i_presses.filter(key__icontains='Teléfono').first().key,
            #     "value": i_presses.filter(key__icontains='Teléfono').first().value
            # },
            # "establecimiento_objetivo": {
            #    "name": i_presses.filter(key__icontains='Categoría').first().key,
            #     "value": i_presses.filter(key__icontains='Categoría').first().value
            # },
            "establecimiento_ambientes": {
             "name": i_presses.filter(key__icontains='Ambientes del Establecimiento').first().key,
                "value": i_presses.filter(key__icontains='Ambientes del Establecimiento').first().value
            },
            "horario": {
                "name": i_presses.filter(key__icontains='Horario').first().key,
                "value": i_presses.filter(key__icontains='Horario').first().value
            },
            # "numero_atenciones": {
            #     "name": i_presses.filter(key__icontains='Categoría').first().key,
            #     "value": i_presses.filter(key__icontains='Categoría').first().value
            # },
            # "infraestructura": {
            #     "name": i_presses.filter(key__icontains='Categoría').first().key,
            #     "value": i_presses.filter(key__icontains='Categoría').first().value
            # }
        }
    ]
    
    
    return JsonResponse(response, safe=False)


def establecimientos(request):
    
    departamento = request.GET.get('departamento', default="01")
    provincia = request.GET.get('provincia', default="02")
    distrito = request.GET.get('distrito', default="02")
    
    establecimientos = get_establecimientos(distrito, provincia, departamento).value
    
    return JsonResponse(establecimientos, safe=False)