# max sub-array..
# a=[10,20,30]
a=list(map(int,input().split()))
m=float('-inf')
n=len(a)

def maximum_sub_array(a,n,m):

    # loop-1
    for i in range(n):
        # loop-2
        for j in range(i,n):
            sum=0
            # loop-3
            for k in range(i,j+1):
                sum+=a[k]
                # max so farr
                m=max(m,sum)
    return m


print(maximum_sub_array(a,n,m))


