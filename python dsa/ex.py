n=int(input())
# l=n

def pn(n):
    # base case
    if(n==0):
        return

    # odd no print increasing oder...
    if(n%2!=0 ):
        print(n)
    # rec.,odd
    pn(n-1)

    # even.. no print in decreasing oder...
    if(n%2==0):
        print(n)

    



pn(n)
