n=int(input())

# 54321 as output

# funct.. that returns inverse value...
def inverse(n):
    val=n
    sum=0
    i=1
    while val!=0:
        r=val%10
        sum+=i*(int(10**(r-1)))
        val//=10
        i+=1
    return sum

x=inverse(n)
print(x)






