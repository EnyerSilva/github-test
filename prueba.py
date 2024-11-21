from typing import List

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None

    def insertar_al_inicio(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            nodo.siguiente = self.head
            self.head.anterior = nodo
            nodo.anterior = None
            self.head = nodo

    def buscarcon(self, clave):
        actual = self.head
        while actual != None and actual.clave != clave:
            actual = actual.siguiente
        return actual

    def eliminarcon(self, nodo):
        if self.head == None:
            print("La lista esta vacia")
            return
        elif self.head == nodo and nodo.siguiente == None:  # Un solo nodo
            self.head = None
        elif nodo == self.head:  # Nodo al inicio
            self.head = nodo.siguiente
            self.head.anterior = None
        elif nodo.siguiente == None:  # Nodo al final
            nodo.anterior.siguiente = None
        else:  # Nodo en medio
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior
        return ("El elemento no se halla en el hash")


class TablaHashEncadenamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = [ListaDoblementeEnlazada() for _ in range(capacidad)]

    def funcion_hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, nodo):
        clave = nodo.clave
        indice = self.funcion_hash(clave)
        #nodo = Nodo(clave, valor)
        self.tabla[indice].insertar_al_inicio(nodo)

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        nodo = self.tabla[indice].buscarcon(clave)
        if nodo:
            return nodo.valor
        return None

    def eliminar(self, nodo):
        clave = nodo.clave
        indice = self.funcion_hash(clave)
        return self.tabla[indice].eliminarcon(nodo)

# Ejemplo de uso
tabla = TablaHashEncadenamiento(10)
c = Nodo('banana', 9)
d = Nodo('pera', 5)
e = Nodo('manzana', 10)

tabla.eliminar(d)

