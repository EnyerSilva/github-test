from typing import List

def MergeSort(A, p, r):

    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    n = q - p + 1
    m = r - q
    L = [0]*(n + 1)
    R = [0]*(m + 1)
    for i in range(n):
        L[i] = A[p + i]
    for j in range(m):
        R[j] = A[q + 1 + j]
    L[n] = float('inf')
    R[m] = float('inf')
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def InsertionSort(A, p, r):
    for j in range(1, r+1):
        actual = A[j]
        i = j - 1
        while i >= p and A[i] > actual:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = actual
