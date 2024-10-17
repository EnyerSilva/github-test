import random
def Randomized_Quicksort(A:list[int], p:int, r:int):
    if (p < r):
        q = Randomized_Partition(A, p, r)
        Randomized_Quicksort(A, p, q - 1)
        Randomized_Quicksort(A, q + 1, r)
        return A
    else:
        return A

def Randomized_Partition(A:list[int], p:int, r:int):
    i = random.randint(p, r)
    A[i] , A[r] = A[r] , A[i]
    return Partition(A, p, r)

def Partition(A:list[int], p:int, r:int):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1], A[r] = A[r], A[i + 1]
    return i + 1

arr = [2, 8, 7, 1, 3, 5, 6, 4]
print(arr)
print(Randomized_Quicksort(arr,0,len(arr)-1))