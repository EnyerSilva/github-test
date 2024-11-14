from typing import List

class Queue(object):
    #capacity = 10
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.array = [0] * capacity
        self.tail = 0
        self.nelements = 0

    def Queue_Empty(self):
        return self.nelements == 0
    
    def Enqueue(self, x):
        if self.nelements == self.capacity:
            raise Exception("Queue overflow")
        self.array[self.tail] = x
        self.tail += 1
        if self.tail >= self.capacity:
            self.tail = 0
        self.nelements += 1

    def Dequeue(self):
        if self.Queue_Empty():
            raise Exception("Queue underflow")
        x = self.array[self.head]
        self.head += 1
        if self.head >= self.capacity:
            self.head = 0
        self.nelements -= 1
        return x
    
    def Print_Queue(self):
        if self.Queue_Empty():
            print("Stack is empty")         # esta funcion es para ver el funcionamiento de la cola
        else:
            for i in range(self.capacity):
                print(self.array[i], end="  ")
            print()
    
queue = Queue(12)
queue.Dequeue()
queue.Print_Queue()

