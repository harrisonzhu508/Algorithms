#Sorting Algorithms
#Bubble Sort
def bubblesort(A):
    #dummy variables key and t
    key = 0
    t = 0
    for i in xrange(len(A)-1,-1,-1):
        key = A[0]
        t = 0
        while t < i:
            if key > A[t+1]:     
                A[t] = A[t+1]
                A[t+1] = key
                key = A[t+1]
            else:
                key = A[t+1]
            t = t + 1
    return A
            
#insertion sort
def insertionsort(A):
    for j in xrange(1,len(A)):
        key = A[j]
        #insert A[j] into sorted sequence A[1,...,j-1]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    print A

#Divide and conquer sorting
#merge sort
#we need infinity
import math
#define merge first
def merge(A,p,q,r):
    n1 = q - p
    n2 = r - q -1
    print n1
    print n2
    #divide into left and right arrays
    L = [None]*(n1 + 2)
    R = [None] *(n2 + 2)
    for i in xrange(n1+1):
        L[i] = A[p + i]
    for j in xrange(n2+1):
        R[j] = A[q + j + 1]
    L[n1+1] = float('inf')
    R[n1+1] = float('inf')
    print L
    print R
    #merge them
    i = 0
    j = 0
    for k in xrange(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    print A
#now that we have a well-defined merge operation, we can trivially obtain mergesort
def mergesort(A,p,r):
     if p<r:
         q = int(math.floor((p+r)/2))
         print q
         mergesort(A,p,q)
         mergesort(A,q+1,r)
         merge(A,p,q,r)
    

    
                
                