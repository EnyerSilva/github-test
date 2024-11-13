from typing import List

class Stack(object):
    #capacity = 10
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = [0] * capacity

    def Stack_Empty(self):
        return self.top == 0
    
    def Stack_Push(self, x):
        if self.top == self.capacity:
            raise Exception("Stack overflow")
        self.top += 1
        self.array[self.top - 1] = x

    def Stack_Pop(self):
        if self.top == self.capacity:
            raise Exception("Stack underflow")
        self.top = self.top - 1
        return self.array[self.top] # No se le puso self.array[self.top + 1] porque en stack_push
                                    # se le suma 1 a top para añadir el siguiente, luego al restarle
                                    # a top en Stack_Pop se esta sobre el ultimo elemento insertado, 
                                    # y se procede a eliminar ese 
    
    def Print_Stack(self):
        if self.Stack_Empty():
            print("Stack is empty")         # esta funcion es para ver el funcionamiento de la pila
        else:
            for i in range(self.capacity):
                print(self.array[i], end="  ")
   
stack = Stack(5)
stack.Stack_Push(10)
stack.Stack_Push(40)
stack.Stack_Push(420)
stack.Stack_Push(55)
stack.Print_Stack()
#print(stack.top)
print(stack.Stack_Pop())
stack.Print_Stack()
stack.Stack_Push(58)
stack.Print_Stack()
#pila.Stack_Push(10)
#pila.Stack_Push(10)
#print(pila.Stack_Empty)
#stack.Stack_Empty()