a=[60,50,20,10,40,30]

def partition(a,l,h):

    i=l
    pivot=a[h]
    for j in range(l,h):
        if a[j]<pivot:
            # swap..
            a[i],a[j]=a[j],a[i]
            i+=1
        else:
            j+=1

    # pivot abhi bhi last hai , so swap...
    a[i],a[h]=a[h],a[i]
    # return pivot index value , which is swaped , 
    return i 





def f(a,l,h):
    # bc
    if l>=h:
        return

    # sub-problem..
    # partition..
    # low- high ...
    # pi -->pivot index
    pi=partition(a,l,h)

    # from low to  pivot-1...
    f(a,l,pi-1)

    # from pivot+1 to high
    f(a,pi+1,h)


f(a,0,len(a)-1)
print(a)








# print(*a)

