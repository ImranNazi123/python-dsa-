# leetcode...
# a=[0,1,0,2,1,0,1,3,2,1,2,1]
a=[2,3,5,3,2]
# a=[5,3,1,2,7,4,1,6]
n=len(a)

def x(a,n):
    li=[None]*n
    # li=[]
    ri=[None]*n
    li[0]=a[0]
    for i in range(1,n):
        # left max
        li[i]=max(li[i-1],a[i])

    print(li,end=" ")

    ri[n-1]=a[n-1]
    # right max
    for j in range(n-2,-1,-1):
        ri[j]=max(ri[j+1],a[j])

    print(ri,end=" ")


    sum=0
    for i in range(n):
        sum+=min(li[i],ri[i])-a[i]

    return sum
    


    # print(ri)
        
   

print(x(a,n))
# x(a,n)

