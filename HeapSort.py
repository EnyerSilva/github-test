def maxHeapify(A, i):
    global n
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
        maxHeapify(A, largest)

def buildMaxHeap(A):
    global n
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(A, i)


def Heapsort(A):
    global n
    n = len(A)
    buildMaxHeap(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        n = n - 1
        maxHeapify(A, 0)
    return A
