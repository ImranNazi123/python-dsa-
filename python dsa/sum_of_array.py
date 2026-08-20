a=[10,20,30,40,50,60]
# solving recursively...
# o/p:150...
n=len(a)

def sum_arr(a,n,i=0):
    # bc
    if i==n:
        return 0
    
    
    # sub problem..
    x=sum_arr(a,n,i+1)
    return a[i]+x

print(sum_arr(a,n,))

    
