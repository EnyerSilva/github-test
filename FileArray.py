import random
def FileArrayRandom (FileName:str, n:int, i:int, f:int):
    arreglo_random = []
    for j in range(n):
        arreglo_random.append(random.randint(i,f))
    arreglo_string = [str(elem) + "\n" for elem in arreglo_random]
    file = open(FileName, "x")
    file = open(FileName, "w")
    file.writelines(arreglo_string)

def FileArrayNoRepeat (FileName:str, n:int, i:int, f:int):
    arreglo = []
    while len(arreglo) < n:
        var = random.randint(i,f)
        if ((f - i) < n):
            return print(f"Ingrese un un rango cuya diferencia (fin - inicio) sea mayor o igual a: {n}")
        elif (var not in arreglo):
            arreglo.append(var)
    arreglo_string = [str(elem) + "\n" for elem in arreglo]
    file = open(FileName, "x")
    file = open(FileName, "w")
    file.writelines(arreglo_string)

def ArrayToFile (FileName:str,A:list[int], n:int, i:int, f:int):
    arreglo_string = [str(elem) + "\n" for elem in A]
    file = open(FileName, "x")
    file = open(FileName, "w")
    file.writelines(arreglo_string)

def FileToArray (FileName:str):
    file = open(FileName, "r")
    lineas = file.readlines()
    arreglo = []
    for k in lineas:
        arreglo.append(int(k.strip()))
    return arreglo
