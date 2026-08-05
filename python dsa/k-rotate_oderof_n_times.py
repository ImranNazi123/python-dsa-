n=7
# rotate..k
k=3

a=[10,20,30,40,50,60,70]

def rotate(i,j):
    # loop
    
    while i<j:
        # swap
        t=a[i]
        a[i]=a[j]
        a[j]=t
        # upd..
        i+=1
        j-=1




# fun...
rotate(0,n-1)
rotate(0,k-1)
rotate(k,n-1)

print(a)