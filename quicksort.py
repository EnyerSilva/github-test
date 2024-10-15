from typing import List


def Partition(A, p, r):
    x = A[r]                                           #Elemento Pivote
    i = p - 1
    j = p
    for j in range(p,r):
        if (A[j] <= x):
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1], A[r] = A[r], A[i + 1]
    return i + 1

def QuickSort (A, p, r):
    if (p < r):
        q = Partition(A, p, r)     
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
        return A
    else:
        return A

arr = [100,200,500,300,1000,900,800,700,600,3,2,1,0,-1,-2]
print(arr)
print(QuickSort(arr,0,len(arr)-1))