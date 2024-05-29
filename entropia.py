import math
from collections import Counter

def calcular_entropia(texto):
    frecuencia = Counter(texto)
    
    longitud_texto = len(texto)
    
    entropia = 0.0
    for freq in frecuencia.values():
        probabilidad = freq / longitud_texto
        entropia -= probabilidad * math.log2(probabilidad)
    
    return entropia

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

nombre_archivo = 'lectura.txt'

contenido = leer_archivo(nombre_archivo)

entropia = calcular_entropia(contenido)

print(f"La entropía del archivo '{nombre_archivo}' es: {entropia}")