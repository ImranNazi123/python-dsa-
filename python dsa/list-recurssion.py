l=[1,2,3,4,5,7,6]
key=7777


def search(l,i,key):
    if l[i]==key:
        print(i)
        # return True
    # elif i==0:

    elif i>0:
        search(l,i-1,key)
    else:
        print("no values found...")

search(l,len(l)-1,key)
    



        













def decend(l,i):
    if i==0:
        print(l[i])
    else:
        print(l[i])
        decend(l,i-1) 



# decend(l,len(l)-1)






def pnum(l,i):
    if i==0:
        print(l[i])
    else:
        pnum(l,i-1)
        print(l[i])


# pnum(l,len(l)-1)









def findmax(l,i):

    if i==0:
        return l[i]
    else:
        return max(l[i],findmax(l,i-1))
    
# print(findmax(l,len(l)-1))

   