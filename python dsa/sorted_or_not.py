# time:0(n)
# space:0(n)
a=list(map(int,input().split()))

def f(a,i=0):
    # bc
    if i==len(a)-1:
        return True

    # sub-problem
    return a[i]<a[i+1] and f(a,i+1)

print(f(a,))
