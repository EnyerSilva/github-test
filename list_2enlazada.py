from typing import List

class Nodo(object):
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None
        self.lista = None

class double_list(object):
    def __init__(self):
        self.head = None

    def List_Search(self, k):
        x = self.head
        while x != None and x.data != k:
            x = x.next
        return x
    
    def List_Insert(self, x):
        if self.head == None:
            nuevo_nodo = Nodo(x)
            self.head = nuevo_nodo
        else:
            nuevo_nodo = Nodo(x)
            nuevo_nodo.next = self.head
            self.head.prev = nuevo_nodo
            self.nuevo_nodo = None
            self.head = nuevo_nodo
            return self.head
        
    def List_Delete(self, x):
        # Revisamos si la lista esta vacia
        if self.head == None:
            print("La lista esta vacia")
            return
        # Revisamos si la lista solo tiene un nodo
        if self.head.next == None:
            if self.head.data == x:
                self.head = None
            else:
                print("Elemento no encontrado")
        # Revisamos si esta al inicio
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        # Revisamos dentro de la lista
        apuntador = self.head
        while apuntador.next is not None:
            if apuntador.data == x:
                break
            apuntador = apuntador.next
        if apuntador.next is not None:
            apuntador.prev.next = apuntador.next
            apuntador.next.prev = apuntador.prev
        else:
            # Por si esta al final
            if apuntador.data == x:
                apuntador.prev.next = None
            else:
                return ("Elemento no encontrado")
    
    def print_list(self):
        if self.head == None:
            print("La lista esta vacia")
        else:
            current = self.head
            strin = " "
            while current != None:
                strin += str(current.data) + " ,"
                current = current.next
            print(strin)


class sentinelas(object):
    def __init__(self):
        # Inicialización del nodo sentinela
        self.s = Nodo()
        self.s.next = self.s
        self.s.prev = self.s
    
    def List_Search_s(self, k):
        x = self.s.next
        while x != self.s and x.k != k:
            x = x.next
        return x

    def List_insert_s(self, x):
        nuevo_nodo = Nodo(x)
        last = self.s.prev
        nuevo_nodo.next = self.s
        nuevo_nodo.prev = last
        last.next = nuevo_nodo
        self.s.prev = nuevo_nodo

    def List_Delete_s(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        x.next = None
        x.prev = None

class FreeList(object):
    def __init__(self):
        self.head = None

    def Allocate_Object(self,k):
        if self.head is None:
            return Nodo(k)
        else:
            nodo = self.head
            self.head = self.head.next
            nodo.k = k
            nodo.next = None
            nodo.prev = None
            return nodo

    def Free_Object(self, x):
        x.next = self.head
        self.head = x


lista = double_list()
lista.List_Insert(5)
lista.List_Insert(4)       
lista.List_Insert(8)       
#print(lista.List_Search(8))
lista.print_list()
lista.List_Delete(4)
lista.print_list()
