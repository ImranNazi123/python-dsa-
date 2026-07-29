n=int(input())

def fib(n):
    # base case ...
    if n==1 or n==0:
        return n

    # recursion..
    a=fib(n-1)
    b=fib(n-2)

    return a+b

print(fib(n))
    