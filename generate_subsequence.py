def f(a,out,i):
    # bc
    if i==len(a):
        print(" ".join(out))
        return
    # sub-prob
    # recursive call...
    # include
    out.append(a[i])
    f(a,out,i+1)
    # undo back tracking
    out.pop()
    # exclude
    f(a,out,i+1)



a=input()
out=[]
f(a,out,0)

# print(out)

