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
