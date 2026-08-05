n=int(input())

def bin(n):
    # bc..
    if n==0:
        return ""

    # sub-prob...
    x=bin(n//2)

    return x+str(n%2)

print(bin(n))
