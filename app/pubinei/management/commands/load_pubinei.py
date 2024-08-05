from django.core.management.base import BaseCommand
from tqdm import tqdm
from app.pubinei.models import Pubinei, Poblacion
import pandas
from app.helpers.services import convert_to_slug
import json
from app.NBI.models import NBI
import os

class Command(BaseCommand):
    
    ruta_carpeta = './excels/pubinei/'
    
    encabezados = [
        "IDCCPP",
        "DEPARTAMENTO",
        "PROVINCIA",
        "DISTRITO",
        "Nombre centro poblado",
        "X_COOR",
        "Y_COOR",
        "AREA MVCS",
        
        # Población Censada Total
        "poblacion.totalPobladores",
        "poblacion.cantidadVarones",
        "poblacion.porcentajeVarones",
        "poblacion.cantidadMujeres",
        "poblacion.porcentajeMujeres",
        
        # Población Censada Total por grupos de edad
        "Menos de un año",
        "Menos de un año (%)",
        "poblacion.de0a5",
        "poblacion.de0a5Porcentaje",
        "poblacion.de6a14",
        "poblacion.de6a14Porcentaje",
        "poblacion.de15a29",
        "poblacion.de15a29Porcentaje",
        "poblacion.de30a44",
        "poblacion.de30a44Porcentaje",
        "poblacion.de45a65",
        "poblacion.de45a65Porcentaje",
        "poblacion.de65amas",
        "poblacion.de65amasPorcentaje",
        
        # Población en viviendas particulares por acceso a servcios de agua, saneamiento y alumbrado por red pública
        "Población en viviendas particulares",
        "Población Con acceso a agua por red pública 1/",
        "Población Con acceso a agua por red pública (%) 1/",
        "Población Sin acceso a agua por red pública",
        "Población Sin acceso a agua por red pública (%)",
        "Población Con servicio de alcantarillado u otras formas sanitarias de dispodicion de excretas 2/",
        "Población Con servicio de alcantarillado u otras formas sanitarias de dispodicion de excretas (%) 2/",
        "Población Sin servicio de alcantarillado u otras formas sanitarias de dispodicion de excretas",
        "Población Sin servicio de alcantarillado u otras formas sanitarias de dispodicion de excretas (%)",
        "Población en viviendas Con alumbrado eléctrico",
        "Población en viviendas Con alumbrado eléctrico (%)",
        "Población en viviendas Sin alumbrado eléctrico",
        "Población en viviendas Sin alumbrado eléctrico (%)",
        
        # Población en viviendas particulares por Necesidades Básicas Insatisfechas - NBI
        "necesidades_basicas.Población en viviendas particulares",
        "necesidades_basicas.Población en Viviendas con características físicas inadecuadas 3/",
        "necesidades_basicas.Población en Viviendas con características físicas inadecuadas 3/  (%)",
        "necesidades_basicas.Población en Viviendas con hacinamiento 4/",
        "necesidades_basicas.Población en Viviendas con hacinamiento 4/  (%)",
        "necesidades_basicas.Población en Viviendas sin servicios higiénicos 5/",
        "necesidades_basicas.Población en Viviendas sin servicios higiénicos 5/  (%)",
        "necesidades_basicas.Población en Hogares con niños que no asisten a la escuela 6/",
        "necesidades_basicas.Población en Hogares con niños que no asisten a la escuela 6/  (%)",
        
        # Viviendas particulares con ocupantes presentes por Material de construcción predominante en las paredes
        "vivienda.material.paredes.Total viviendas particulares con ocupantes presentes",
        "vivienda.material.paredes.Pared-Ladrillo o bloque de cemento",
        "vivienda.material.paredes.Pared-Ladrillo o bloque de cemento (%)",
        "vivienda.material.paredes.Piedra o sillar con cal o cemento",
        "vivienda.material.paredes.Piedra o sillar con cal o cemento (%)",
        "vivienda.material.paredes.Adobe",
        "vivienda.material.paredes.Adobe (%)",
        "vivienda.material.paredes.Tapia",
        "vivienda.material.paredes.Tapia (%)",
        "vivienda.material.paredes.Quincha (caña con barro)",
        "vivienda.material.paredes.Quincha (caña con barro) (%)",
        "vivienda.material.paredes.Piedra con barro",
        "vivienda.material.paredes.Piedra con barro (%)",
        "vivienda.material.paredes.Madera (pona, tornillo etc.)",
        "vivienda.material.paredes.Madera (pona, tornillo etc.) (%)",
        "vivienda.material.paredes.Triplay / calamina / estera",
        "vivienda.material.paredes.Triplay / calamina / estera (%)",
        "vivienda.material.paredes.Otro material",
        "vivienda.material.paredes.Otro material (%)",
        
        # Viviendas particulares con ocupantes presentes por Material  predominante en los techos
        "vivienda.material.techos.Techo-Concreto armado",
        "vivienda.material.techos.Techo-Concreto armado (%)",
        "vivienda.material.techos.Madera",
        "vivienda.material.techos.Madera (%)",
        "vivienda.material.techos.Tejas",
        "vivienda.material.techos.Tejas (%)",
        "vivienda.material.techos.Planchas de calamina, fibra de cemento o similares",
        "vivienda.material.techos.Planchas de calamina, fibra de cemento o similares (%)",
        "vivienda.material.techos.Caña o estera con torta de barro o cemento",
        "vivienda.material.techos.Caña o estera con torta de barro o cemento (%)",
        "vivienda.material.techos.Triplay / estera / carrizo",
        "vivienda.material.techos.Triplay / estera / carrizo (%)",
        "vivienda.material.techos.Paja, hoja de palmera y similares",
        "vivienda.material.techos.Paja, hoja de palmera y similares (%)",
        "vivienda.material.techos.Otro material",
        "vivienda.material.techos.Otro material (%)",
        
        # Viviendas particulares con ocupantes presentes por Material  predominante en los pisos
        "vivienda.material.pisos.Piso-Parquet o madera pulida",
        "vivienda.material.pisos.Piso-Parquet o madera pulida (%)",
        "vivienda.material.pisos.Láminas asfálticas, vinílicos o similares",
        "vivienda.material.pisos.Láminas asfálticas, vinílicos o similares (%)",
        "vivienda.material.pisos.Losetas, terrazos, cerámicos o similares",
        "vivienda.material.pisos.Losetas, terrazos, cerámicos o similares (%)",
        "vivienda.material.pisos.Madera (pona, tornillo, etc.)",
        "vivienda.material.pisos.Madera (pona, tornillo, etc.) (%)",
        "vivienda.material.pisos.Cemento",
        "vivienda.material.pisos.Cemento (%)",
        "vivienda.material.pisos.Tierra",
        "vivienda.material.pisos.Tierra (%)",
        "vivienda.material.pisos.Otro material",
        "vivienda.material.pisos.Otro material (%)",
        
        # Viviendas particulares con ocupantes presentes por Régimen de tenencia
        "Alquilada",
        "Alquilada (%)",
        "Propia Sin Titulo",
        "Propia Sin Titulo (%)",
        "Propia Con Titulo",
        "Propia Con Titulo (%)",
        "Cedida",
        "Cedida (%)",
        "Otra forma",
        "Otra forma (%)",
        
        # Población de 15 y más años
        "educacion.Total",
        "educacion.analfabetismo.Población sin saber leer ni escribir",
        "educacion.analfabetismo.Tasa de Analfabetismo de 15 y más años",
        
        # Nivel educativo de la población de 15 y más años
        "educacion.nivel.Sin Nivel o Inicial",
        "educacion.nivel.Sin Nivel o Inicial (%)",
        "educacion.nivel.Primaria (Incluye basica)",
        "educacion.nivel.Primaria (Incluye basica) (%)",
        "educacion.nivel.Secundaria",
        "educacion.nivel.Secundaria (%)",
        "educacion.nivel.Superior No Universitaria",
        "educacion.nivel.Superior No Universitaria (%)",
        "educacion.nivel.Superior universitaria (Incluye posgrado)",
        "educacion.nivel.Superior universitaria (Incluye posgrado) (%)",
        
        # Población por afiliación de seguro de salud (Pueden tener más de un seguro de salud)
        "salud.Seguro Integral de Salud (SIS)",
        "salud.Seguro Integral de Salud (SIS) (%)",
        "salud.ESSALUD",
        "salud.ESSALUD (%)",
        "salud.Seguro de fuerzas armadas o policiales",
        "salud.Seguro de fuerzas armadas o policiales (%)",
        "salud.Seguro privado de salud",
        "salud.Seguro privado de salud (%)",
        "salud.Otro seguro",
        "salud.Otro seguro (%)",
        "salud.Ningún seguro",
        "salud.Ningún seguro (%)"
    ]
    
    def handle(self, *args, **kwargs):
        
        nombres_archivos_excels = self.leer_nombres_excel(self.ruta_carpeta)
        
        for nombre_archivo_excel in nombres_archivos_excels:
            nombre_completo_archivo_excel = os.path.join(self.ruta_carpeta, nombre_archivo_excel)
            
            dataframe = pandas.read_excel(nombre_completo_archivo_excel, names=self.encabezados)
            nombre_columnas = dataframe.columns
            # print(dataframe.head())
            
            
            barra_progreso = tqdm(
                total=dataframe.shape[0]
            )
            for index, row in dataframe.iterrows():
                departamento = None
                provincia = None
                distrito = None
                idccpp = None
                key = None
                value = None
                
                for nombre_columna in nombre_columnas:

                    if nombre_columna == "DEPARTAMENTO":
                        departamento = row[nombre_columna]

                    elif nombre_columna == "PROVINCIA":
                        provincia = row[nombre_columna]

                    elif nombre_columna == "DISTRITO":
                        distrito = row[nombre_columna]

                    elif nombre_columna == "IDCCPP":
                        idccpp = row[nombre_columna]

                    else:
                        key = nombre_columna
                        value = row[nombre_columna]

                    if key is not None and value is not None and departamento is not None and provincia is not None and distrito is not None and idccpp is not None:
                        barra_progreso.set_description(departamento)
                        poblacion = Poblacion(
                            departamento=departamento,
                            provincia=provincia,
                            distrito=distrito,
                            idccpp=idccpp,
                            key=key,
                            value=value
                        )
                        poblacion.save()
                        key = None
                        value = None

                barra_progreso.update(1)    
            
    def leer_nombres_excel(self, ruta_carpeta):
        nombre_archivos_y_carpetas = os.listdir(ruta_carpeta)
        
        nombre_archivos_excels = []
        for nombre_archivo_o_carpeta in nombre_archivos_y_carpetas:
            nombre_completo_archivo_o_carpeta = os.path.join(ruta_carpeta, nombre_archivo_o_carpeta)
            
            if not os.path.isfile(nombre_completo_archivo_o_carpeta):
                continue
            else:
                nombre_archivo = nombre_archivo_o_carpeta
            
            if nombre_archivo.endswith('.xlsx') and not nombre_archivo.startswith('~$'):
                nombre_archivos_excels.append(nombre_archivo)
                
        nombre_archivos_excels.sort()
                
        return nombre_archivos_excels