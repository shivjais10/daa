
def selection(a):
    l=len(a)
    for i in range (0,l):
        min =i
        for j in range(i+1,l):
            if a[j]<a[min]:
                min=j

        a[i], a[min] = a[min], a[i]

    print a
arr=list(map(int,raw_input().strip().split()))
selection(arr)