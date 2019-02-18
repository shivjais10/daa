
def bubble(a):
    l=len(a)
    for i in range (0,l):

        for j in range(l-1,i,-1):
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]




arr=list(map(int,raw_input().strip().split()))
bubble(arr)