from django.shortcuts import render
from django.http import JsonResponse
from .services import get_pubinei_data, get_poblacion_data
from django.db.models import Q

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
        idccpp = request.GET.get('idccpp', default="101010001,101010002")

        poblaciones = list(get_poblacion_data(idccpp))
        print(len(poblaciones))
        # return JsonResponse(
        #     [], 
        #     safe=False
        # )
        response = {
            "poblacion": {
                title: round(float(next((p.value for p in poblaciones if 'poblacion.' + title in p.key), 0)), 2)
                for title in [
                    "cantidadVarones",
                    "cantidadMujeres",
                    "totalPobladores",
                    "porcentajeVarones",
                    "porcentajeMujeres",
                    # "de0a14",
                    # "de0a14Porcentaje",
                    # "de14a29",
                    # "de14a29Porcentaje",
                    # "de30a44",
                    # "de30a44Porcentaje",
                    # "de44a64",
                    # "de44a64Porcentaje",
                    # "de65amas",
                    # "de65amasPorcentaje",
                    "de0a5",
                    "de0a5Porcentaje",
                    "de6a14",
                    "de6a14Porcentaje",
                    "de15a29",
                    "de15a29Porcentaje",
                    "de30a44",
                    "de30a44Porcentaje",
                    "de45a65",
                    "de45a65Porcentaje",
                    "de65amas",
                    "de65amasPorcentaje",
                ]
            },
            # "pet": {
            #     "totalPet": 721,
            #     "de15a29": 234,
            #     "de15a29Porcentaje": 32.45,
            #     "de30a44": 224,
            #     "de30a44Porcentaje": 31.07,
            #     "de45a64": 173,
            #     "de45a64Porcentaje": 23.99,
            #     "de65amas": 90,
            #     "de65amasPorcentaje": 12.48
            # },
            # Pared-Ladrillo o bloque de cemento
            "vivienda": {
                "total": 339,
                "materiales": [
                    {
                        "categoria": category,  
                        "tipos": [
                            
                            {   
                                "tipo": item.key.replace('vivienda.material.'+word_key+".", '').replace('(%)', ''),
                                "casos": next((p.value for p in poblaciones if item.key.replace('(%)', '').strip() in p.key), 0),
                                "porcentaje": round(float(item.value),2)
                            }
                            for item in poblaciones
                            if 'vivienda.material.'+word_key in item.key and '(%)' in item.key
                        ]
                    }
                    for word_key, category in {
                        "paredes": "Material de las paredes de las viviendas",
                        "techos": "Material predominante en los techos de las viviendas",
                        "pisos": "Material de los pisos de las viviendas",
                    }.items()
                    
                ]
            },
            "salud": {
                "total": 1096,
                # {
                #     "tipo": "Seguro Integral de Salud (SIS)",
                #     "poblacion": 937,
                #     "porcentaje": 85.73
                # },
                "tipo": [
                            
                    {   
                        "tipo": item.key.replace('salud.', '').replace('(%)', ''),
                        "poblacion": next((p.value for p in poblaciones if item.key.replace('(%)', '').strip() in p.key), 0),
                        "porcentaje": round(float(item.value),2)
                    }
                    for item in poblaciones
                    if 'salud.' in item.key and '(%)' in item.key
 
                ]
            },
           
            "educacion": {
                "total": 721,
                "nivel": [
                    # {
                    #     "total": "Sin nivel o Inicial",
                    #     "casos": 89,
                    #     "porcentaje": 12.34
                    # },
                          
                    {   
                        "total": item.key.replace('salud.nivel.', '').replace('(%)', ''),
                        "casos": next((p.value for p in poblaciones if item.key.replace('(%)', '').strip() in p.key), 0),
                        "porcentaje": round(float(item.value),2)
                    }
                    for item in poblaciones
                    if 'educacion.nivel.' in item.key and '(%)' in item.key
                ],
                "analfabetismo": [
                    # {
                    #     "total": "Sabe leer y escribir",
                    #     "casos": 628,
                    #     "porcentaje": 87.10
                    # },
                    {   
                        "total": item.key.replace('educacion.analfabetismo.', '').replace('(%)', ''),
                        "casos": next((p.value for p in poblaciones if item.key.replace('(%)', '').strip() in p.key), 0),
                        "porcentaje": round(float(item.value),2)
                    }
                    for item in poblaciones
                    if 'educacion.analfabetismo.' in item.key and '(%)' in item.key
                ]
            },
            "necesidades_basicas": {
                "total": 516,
                "detalle": [
                    # {
                    #     "categoria": "Población en Viviendas con características físicas inadecuadas",
                    #     "casos": 182,
                    #     "porcentaje": 17.76
                    # },
                    {
                        "categoria": item.key.replace('necesidades_basicas.', '').replace('(%)', ''),
                        "casos": next((p.value for p in poblaciones if item.key.replace('(%)', '').strip() in p.key), 0),
                        "porcentaje": round(float(item.value),2)
                    }
                    for item in poblaciones
                    if 'necesidades_basicas.' in item.key and '(%)' in item.key
                ]
            }
        }
    
        return JsonResponse(
            response, 
            safe=False
        )
        
        