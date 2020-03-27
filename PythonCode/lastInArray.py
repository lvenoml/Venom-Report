def searchLast(A, k):
    if len(A)==0:
        return -1
    if A[len(A)-1]==k:
        return len(A)-1
    else:
        return searchLast(A[:(len(A)-1)], k)
