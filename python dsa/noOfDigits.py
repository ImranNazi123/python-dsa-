import math
n=123456
# val=0
# N=2
# N=no. of times must rotate....

# rotate funct.
   
def rot(n):
    # return int(r*(10**(math.log10(q)+1)))
    return int(math.log10(n))

def nod(n):
    # no. of times must be rotate...
    i=1
    while i<=2:

        r=n%10
        q=n//10
        val= rot(n)
        i+=1
        n=r*(10**(val ))+q
    print(n)
    





nod(n)





















# x=100

# print(int(math.log10(x))+1)