a=[1,2,3,4]
# sum=0

# print(a[0:2])


def SumofSubArr_m2(a):
    #  reduce time complexity......
     i=0
    # col
     while i<len(a):
        sum=0
        j=i
        for j in range(i,len(a)):
            # sum=1
            # sum=3
            # sum=6.....

            sum+=a[j]
            print((i,j),sum)
        i+=1
    




# fun.. to print sum...
def sumofSubarr(a):
    i=0
    # col
    while i<len(a):
        
        # j=i
        for j in range(i,len(a)):
            # for l in a[i:j+1]:
            # l prints from (i-j)
            sum=0
            for l in range(i,j+1):  
                sum+=a[l] 
                # print(a[i:j])
                print((i,j),sum)


            print()
        i+=1
    








def SubArr_m1(a):
    i=0
    # col
    while i<len(a):
        
        # j=i
        for j in range(i,len(a)):
            # for l in a[i:j+1]:
            # l prints from (i-j)
            for l in range(i,j+1):   
                print(a[l],end=" ")
            print()
        i+=1


            


def subArr():
    i=0
    # col
    while i<len(a):
        # row
        j=i
        l=1
        while j<len(a):
            # print(i,j)
            # below print sub-array tog,,,
            print(a[i:j+1])
            j+=1
        i+=1

SumofSubArr_m2(a)

# sumofSubarr(a)

# SubArr_m1(a)

# subArr()



