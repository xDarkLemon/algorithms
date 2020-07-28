def partition(a,p,r):
    pivot=a[r]
    i=p
    for j in range(p,r): # p,...,r-1
        if a[j]<pivot:
            tmp=a[j]
            a[j]=a[i+1]
            a[i+1]=tmp
            i+=1
    tmp=a[i+1]
    a[i+1]=pivot
    a[r]=tmp
    return a,i+1 # partition position

# def partition_(a,p,r):
#     pivot=a[r]
#     i=p
#     j=p
#     for k in range(p,r): # p,...,r-1
#         if a[k]<pivot:
#             tmp=a[k]
#             a[k]=a[i+1]
#             a[i+1]=tmp
#             i+=1
#             j+=1
#         else:
#             j+=1
#     tmp=a[i+1]
#     a[i+1]=pivot
#     a[r]=tmp
#     return a,i+1
            
def quick_sort(a,p,r):
    if p<r:
        a,q=partition(a,p,r)
        a=quick_sort(a,p,q-1)
        a=quick_sort(a,q+1,r)
    return a

