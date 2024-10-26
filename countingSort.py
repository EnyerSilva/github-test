def countingSort(A, B, k):
    C = [0]*(k+1)
    if len(B) < len(A):
        d = len(A) - len(B)
        for i in range(d):
            B.append(0)
    if len(B) > len(A):
        d = len(B)-len(A)
        for i in range(d):
            B.pop()
    n = len(A)
    for j in range(n):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for j in range(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B
print(countingSort([2, 5, 3, 1, 7, 4, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0], 7))