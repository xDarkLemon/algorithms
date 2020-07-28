def counting_sort(a,k): # a[i] is an integer between 0 and k
    n=len(a)
    c=[0] * k
    for i in range(n):
        c[a[i]]+=1
    for i in range(1,k):
        c[i]+=c[i-1]
    b=[0] * n
    for i in range(n):
        b[c[a[i]]-1]=a[i]
        c[a[i]]-=1
    return b
