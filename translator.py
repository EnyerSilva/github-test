from typing import List

def strtoascii(p:str):
    if type(p) == int:
        raise Exception("Ingrese solo texto")
    elif type(p) == float:
        raise Exception("Ingrese solo texto")
    elif len(p) == 0:
        raise Exception("Escriba al menos un caracter")
    else:
        lista = []
        n = len(p)
        for i in range(n):
            lista.append(ord(p[i]))
            i += 1
    return lista

def encryption(arr:List[int]):
    if (len(arr)%2) != 0:
        arr.append(32)
    j = 0
    for i in range(len(arr)):
        if (i%2 == 0):
            arr[i] = arr[i] + (j + 1)
            j += 1
        else:
            arr[i] = arr[i] + (j - 1)
            j += 1
    return(arr)

def decryption(arr:List[int]):
    if (len(arr)%2) != 0:
        arr.append(32)
    j = 0
    for i in range(len(arr)):
        if (i%2 == 0):
            arr[i] = arr[i] - (j + 1)
            j += 1
        else:
            arr[i] = arr[i] - (j - 1)
            j += 1
    return(arr)

def asciitostr(arr:List[int]):
    '''
    Recibe una lista de números de caracteres en formato ASCII
    Y retorna la palabra o caracter original
    '''
    for i in range(len(arr)):
        if type(arr[i]) == str:
            raise Exception("Solo se admiten numeros enteros")
        elif type(arr[i]) == float:
            raise Exception("Solo se admiten numeros enteros")
        else:
            arr[i] = chr(arr[i])
    return ''.join(arr)

palabra = "CODE RED"
print(f"Esta es la palabra original: {palabra}")
palabra = strtoascii(palabra)
print(f"Codigo ASCII de cada una de sus letras: {palabra}")
palabra = encryption(palabra)
print(f"Nivel 1 de Encriptado aplicado: {palabra}")
palabra = asciitostr(palabra)
print(f"Nueva palabra después de nivel 1 de encriptado: {palabra}")
print(" ")
print(f"Ahora desencriptamos la palabra: {palabra}")
palabra = strtoascii(palabra)
print(f"Codigo ASCII de cada una de sus letras: {palabra}")
palabra = decryption(palabra)
print(f"Desencriptando la palabra: {palabra}")
palabra = asciitostr(palabra)
print(f"Palabra original: {palabra}")