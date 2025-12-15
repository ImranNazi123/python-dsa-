
# take 6 input from user 
n=int(input("enter size: "))

# first no , considered to be max....
max=int(input())

# since first no. is max , start with rest no present....
i=2
# range 2-remaining size.....
while i<=n:


    x=int(input())
    
    if max<x:
        max=x
    i+=1    
    
print("max is : ",max)
    
