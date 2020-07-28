import math
def merge(a,p,q,r): # a[p,...,q], a[q+1,...,r] are sorted
    L=[]
    R=[]
    for i in range(p,q):
        L.append(a[i])
    for i in range(q+1,r+1):
        R.append(a[i])
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
    return a

def merge_sort(a,p,r):
    if p<r: # stopping criteria
        q=math.floor((r-p)/2)
        a=merge_sort(a,p,q)
        a=merge_sort(a,q+1,r)
        a=merge(a,p,q,r)
    return a

a=[]
n=len(a)
merge_sort(a,0,n-1)