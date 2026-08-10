n=int(input())
sum=0

def nth_triangle(n):
    # base case..
    if n==1:
        return 1

    # sub-problem...
    x=nth_triangle(n-1)
    return x+n



    

print(nth_triangle(n))

