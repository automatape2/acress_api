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
                "name": i_presses.filter(key__icontains='IPRESS').first().key if i_presses.filter(key__icontains='IPRESS').first() is not None else "",
                "value": i_presses.filter(key__icontains='IPRESS').first().value if i_presses.filter(key__icontains='IPRESS').first() is not None else ""
            },
            "categoria": {
                "name": i_presses.filter(key__icontains='Categoría').first().key if i_presses.filter(key__icontains='Categoría').first() is not None else "",
                "value": i_presses.filter(key__icontains='Categoría').first().value if i_presses.filter(key__icontains='Categoría').first() is not None else ""
            },
            "tipo": {
               "name": i_presses.filter(key__icontains='Tipo de Establecimiento').first().key if i_presses.filter(key__icontains='Tipo de Establecimiento').first() is not None else "",
                "value": i_presses.filter(key__icontains='Tipo de Establecimiento').first().value if i_presses.filter(key__icontains='Tipo de Establecimiento').first() is not None else ""
            },
            "subcategoría": {
              "name": i_presses.filter(key__icontains='Clasificación').first().key  if i_presses.filter(key__icontains='Clasificación').first() is not None else "",
                "value": i_presses.filter(key__icontains='Clasificación').first().value.split('\n')[7] if len(i_presses.filter(key__icontains='Clasificación').first().value.split('\n')) >= 8 else "La línea no existe"
            },
            "estado": {
               "name": i_presses.filter(key__icontains='Estado').first().key  if i_presses.filter(key__icontains='Estado').first() is not None else "",
                "value": i_presses.filter(key__icontains='Estado').first().value if i_presses.filter(key__icontains='Estado').first() is not None else "" 
            },
            "condicion": {
              "name": i_presses.filter(key__icontains='Condición').first().key  if i_presses.filter(key__icontains='Condición').first() is not None else "",
                "value": i_presses.filter(key__icontains='Condición').first().value if i_presses.filter(key__icontains='Condición').first() is not None else "" 
            },
            "diresa": {
               "name": i_presses.filter(key__icontains='DIRESA').first().key  if i_presses.filter(key__icontains='DIRESA').first() is not None else "",
                "value": i_presses.filter(key__icontains='DIRESA').first().value if i_presses.filter(key__icontains='DIRESA').first() is not None else "" 
            },
            "red": {
                "name": i_presses.filter(key__icontains='RED').first().key if i_presses.filter(key__icontains='RED').first() is not None else "",
                "value": i_presses.filter(key__icontains='RED').first().value if i_presses.filter(key__icontains='RED').first() is not None else ""
            },
            "microred": {
             "name": i_presses.filter(key__icontains='MICRORED').first().key if i_presses.filter(key__icontains='MICRORED').first() is not None else "",
                "value": i_presses.filter(key__icontains='MICRORED').first().value if i_presses.filter(key__icontains='MICRORED').first() is not None else ""
            },
            "establecimiento": {
             "name": i_presses.filter(key__icontains='Tipo de Establecimiento').first().key if i_presses.filter(key__icontains='Tipo de Establecimiento').first() is not None else "",
                "value": i_presses.filter(key__icontains='Tipo de Establecimiento').first().value if i_presses.filter(key__icontains='Tipo de Establecimiento').first() is not None else ""
            },
            "establecimiento_ambientes": {
             "name": i_presses.filter(key__icontains='Ambientes del Establecimiento').first().key if i_presses.filter(key__icontains='Ambientes del Establecimiento').first() is not None else "",
                "value": i_presses.filter(key__icontains='Ambientes del Establecimiento').first().value if i_presses.filter(key__icontains='Ambientes del Establecimiento').first() is not None else ""
            },
            "horario": {
                "name": i_presses.filter(key__icontains='Horario').first().key if i_presses.filter(key__icontains='Horario').first() is not None else "",
                "value": i_presses.filter(key__icontains='Horario').first().value if i_presses.filter(key__icontains='Horario').first() is not None else ""
            },
            # "establecimiento_telefono": {
            #    "name": i_presses.filter(key__icontains='Teléfono').first().key,
            #     "value": i_presses.filter(key__icontains='Teléfono').first().value
            # },
            # "establecimiento_objetivo": {
            #    "name": i_presses.filter(key__icontains='Categoría').first().key,
            #     "value": i_presses.filter(key__icontains='Categoría').first().value
            # },
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