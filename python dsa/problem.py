n1=int(input())
n2=int(input())
# val=0


def Print_1(n1,n2,val):
    i=1
    while i<=10:
        val=3*i+2
        if val%n2!=0:
            print(val)
        
        i+=1


def Test1(n1,n2):
    ct=1
    i=1
    while ct<=10:
        val=3*i+2
        if val%n2!=0:
            print(val)
            ct+=1
        

        
        i+=1


# Print_1(n1,n2,val)
Test1(n1,n2)




# -----------output-------
# input:10 , 4 

# output must be: total 10 numbers , !=0

