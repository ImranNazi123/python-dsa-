n=3
a=0
b=1


def fibtail(n,a,b):
    if n==0:
        return a
    else:
        return fibtail(n-1,b,a+b)
    




def fib(n):
    # head rec....
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+(n+2)

# x=fib(n)
# print(x)

x=fibtail(n,a,b)
print(x)


