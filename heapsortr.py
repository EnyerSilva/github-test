def maxHeapify(A, n, i):
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    if leftChild < n and A[leftChild] > A[i]:
        largest = leftChild
    else:
        largest = i
    if rightChild < n and A[rightChild] > A[largest]:
        largest = rightChild
    
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, n, largest)

def buildMaxHeap(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(A, n, i)


def Heapsort(A):
    n = len(A)
    buildMaxHeap(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        maxHeapify(A, i, 0)
    return A