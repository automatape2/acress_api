from django.http import JsonResponse
from .services import get_centro_poblados, get_data_midis

def index(request):
    departamento = request.GET.get('departamento', default="Lima").upper()
    provincia = request.GET.get('provincia', default="Lima").upper()
    distrito = request.GET.get('distrito', default="Lima").upper()
    centropoblado = request.GET.get('centropoblado', default="1501010001-LIMA").upper()

    midis = get_data_midis(distrito, provincia, departamento, centropoblado)
    total_midis = sum(float(midi.value.replace(",", "")) for midi in midis)
    
    midis_agua = midis.filter(key__icontains='agua')
    total_midis_agua = sum(float(midi_agua.value.replace(",", "")) for midi_agua in midis_agua)
    
    midis_ocupado = midis.filter(key__icontains='ocupad')
    total_midi_ocupado = sum(float(midi_ocupado.value.replace(",", "")) for midi_ocupado in midis_ocupado)
    
    midis_desague = midis.filter(key__icontains='saneamient')
    total_midis_desague = sum(float(midi_desague.value.replace(",", "")) for midi_desague in midis_desague)
    
    midis_electricidad = midis.filter(key__icontains='electr')
    total_midis_electricidad = sum(float(midi_electricidad.value.replace(",", "")) for midi_electricidad in midis_electricidad)

    response = {
        "vivienda": {
            "total": total_midis,
            "ocupada": total_midi_ocupado,
            "porcentajeocupada": round(total_midi_ocupado  / total_midis * 100,2),
            "otracondicion": total_midis - total_midi_ocupado,
            "porcentajeotracondicion": round((total_midis - total_midi_ocupado)  / total_midis * 100,2)
        },
        
        "agua": {
            "total": total_midis_agua,
            "categorias": [
                {
                    "nombre": midi_agua.key,
                    "casos": int(midi_agua.value.replace(",", "")),
                    "porcentaje": round(float(midi_agua.value.replace(",", ""))  / total_midis_agua * 100,2)
                }
                for midi_agua in midis_agua
            ]
        },
        "desague": {
            "total": total_midis_desague,
            "categorias": [
                {
                    "nombre": midi_desague.key,
                    "casos": int(midi_desague.value.replace(",", "")),
                    "porcentaje": round(float(midi_desague.value.replace(",", ""))  / total_midis_desague * 100,2)
                }
                for midi_desague in midis_desague
            ]
        },
        "electricidad": {
            "total": total_midis_electricidad,
            "categorias": [
                {
                    "nombre": midi_electricidad.key,
                    "casos": int(midi_electricidad.value.replace(",", "")),
                    "porcentaje": round(float(midi_electricidad.value.replace(",", ""))  / total_midis_electricidad * 100,2)
                }
                for midi_electricidad in midis_electricidad
            ]
        }
    }
   
    return JsonResponse(response, safe=False)

def centros_poblados(request):
    departamento = request.GET.get('departamento', default="Lima").upper()
    provincia = request.GET.get('provincia', default="Lima").upper()
    distrito = request.GET.get('distrito', default="Lima").upper()
 
    # new filter, TODO: implement does not work if you do not add
    centro_poblado_request = request.GET.get('centros_poblado', default="1501010001-Lima").upper()
   
    centros_poblados = get_centro_poblados(distrito, provincia, departamento, centro_poblado_request).value
    
    return JsonResponse(centros_poblados, safe=False)