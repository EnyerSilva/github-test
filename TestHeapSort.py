import sys
import time
from heapsortr import *

archivo = sys.argv[1]
file = open(archivo, "r")
lineas = file.readlines()
arreglo_inicial = []
for k in lineas:
    arreglo_inicial.append(int(k.strip()))

n = int(len(arreglo_inicial))
algoritmo = "HeapSort"
inicio = time.time()
arreglo_ordenado = Heapsort(arreglo_inicial)
arreglo_strings = [str(elem) + "\n" for elem in arreglo_ordenado]
fin = time.time()
archivo2 = open("ArchivoNumeros.sorted" , "x")
archivo2 = open("ArchivoNumeros.sorted" , "w")
archivo2.writelines(arreglo_strings)
archivo2.close()
tiempo_Transcurrido = (fin-inicio) * 1000

print(algoritmo, n, tiempo_Transcurrido)

