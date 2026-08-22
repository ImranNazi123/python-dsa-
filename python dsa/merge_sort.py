# time:0(nlogn)
# space:0(n)
# a=list(map(int,input().split()))
# a=[60,50,40,30,20,10]
a=[5,2,3,1]
# a=[10,30,50,70,80,90]

# b=[20,40,60]

n=len(a)

def f(a,l,h,mid):
    # merge 
    i=l
    j=mid+1
    temp=[]
    # loop
    # i to mid and mid+1 to h..
    while i<=mid and j<=h:
        if a[i]<=a[j]:
            # swap
            temp.append(a[i])
            i+=1
        else:
            temp.append(a[j])
            j+=1

    # to print remaining ...
    while i<=mid:
        temp.append(a[i])
        i+=1

    while j<=h:
        temp.append(a[j])
        j+=1

    # place back in array a from temp..
    a[l:h+1]=temp













def merge(a,l=0,h=len(a)-1):
    # bc
    if l==h:
        return

    # mid
    mid=(l+h)//2

    # sub problem left sort..
    # low se mid tak....
    merge(a,l,mid)

    # sub problem right sort
    # mid+1 se high tak
    merge(a,mid+1,h)

    # merge and sort,,..
    f(a,l,h,mid)


merge(a,)
print(a)
