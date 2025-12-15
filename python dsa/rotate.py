a=[1,2,3,4,5,6]
n=int(input())

def reverse(a,i,j):
    si=i
    ei=j
    while si<ei:
        # swap no..
        t=a[si]
        a[si]=a[ei]
        a[ei]=t
        si+=1
        ei-=1





def rotate(a,k):
    # k is no. of times value is to be rotated ...
    k=k%len(a)

    # suppose k=2 is to be rotated ..
    # reversing no. from 0-a.length..
    reverse(a,0,len(a)-1)
    # reversing no. from 0-1 for k=2...
    reverse(a,0,k-1)
    # reversing from remaing , ie k=2 to a.length...
    reverse(a,k,len(a)-1)





rotate(a,n)
print(a)
