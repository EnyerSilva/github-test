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

print(asciitostr(strtoascii("Parangaricutinimicuaro")))
         
