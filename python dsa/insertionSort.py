a=[1,2,4,5,3]
# b=[1,3,4,5,2]
b=[5,1,3,4,2]


def insert_1(b):
    # insert last no==1
    t=len(b)-1
    lst=b[t]
    flag=True

    # insertion...
    # start index 3 end at 0 ie. (3-0)
    for i in range (len(b)-2,-1,-1): 
        if b[i]>lst:
            b[i+1]=b[i]
        else:
            flag=False
            b[i+1]=lst
            break
    
    else:

        # if flag==True:
                b[i]=lst 

    # else:
    #     if flag==True:
    #         a[0]=lst
        



        
        







# print(a)






def insert(a):
    t=a[len(a)-1]
    l=a[t]

    for i in range(len(a)-2,-1,-1):
        if a[i]>t:
            # swap
            a[i+1]=a[i]
        
        else:
            a[i+1]=t
            break

    # # for printing in decreasing order.....
    # for i in range(len(a)-1,-1,-1):
    #     print(a[i],end=" ")

# insert(a)
insert_1(b)

# print(a)
print(b)
