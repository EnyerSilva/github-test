def QuickSort (A:list[int], p:int, r:int):
    if (p < r):
        q = Partition(A, p, r)     
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
        return A
    else:
        return A

def Partition(A:list[int], p:int, r:int):
    x = A[r]                                           #Elemento Pivote
    i = p - 1
    j = p
    for j in range(p,r):
        if (A[j] <= x):
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1], A[r] = A[r], A[i + 1]
    return i + 1

arr = [100,200,500,300,1000,900,800,700,600,3,2,1,0,-1,-2]
print(arr)
print(QuickSort(arr,0,len(arr)-1))