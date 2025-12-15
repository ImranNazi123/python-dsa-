import math
# print armstrong no, from 1-1000
# sum=0

# no. of digit...
def nod(i):
    return int(math.log10(i))+1


# check armstrong or not....
def isArms():
    i=1
    while i<=1000:
        x=nod(i)
        y=i
        sum=0

        while y!=0:
            r=y%10
            sum+=r**x
            y//=10
        printAllArms(sum,i)
        

        i+=1







# print armstrong no
def printAllArms(sum,i):
    if sum==i:
        print(i)
    else:
        return
    
    
isArms()
