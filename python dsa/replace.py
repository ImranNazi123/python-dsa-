# wc:0(n^2)
# space:0(n) due to function call stack....

def f(a,i):
    # bc
    if i>=len(a)-1:
        return

    # rec.. call
    if a[i]=="p" and a[i+1]=="i":
        # slicing..
        a[i:i+2]=list("3.14")
        # recursion call..
        f(a,i+4)
    else:
        f(a,i+1)
    



# a=list(input())
a=list("pifghh")
# out=[]
f(a,0)
print(" ".join(a))
