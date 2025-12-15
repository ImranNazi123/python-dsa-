a=[5,3,4,1,2]

si=0
ei=len(a)-1


while si<ei:
    t=a[si]
    a[si]=a[ei]
    a[ei]=t

    # updt...
    si+=1
    ei-=1

print(a)


# print(a[4])