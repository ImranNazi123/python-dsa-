a=[0,4,6,8,9]

def rev(a):
    # for i in range(len(a)):
    #     print(a[i])
    si=0
    ei=len(a)-1

    while si<ei:
        t=a[si]
        a[si]=a[ei]
        a[ei]=t
        # print(a[si])
        si+=1
        ei-=1
    
    for i in range(len(a)):
        print(a[i])





rev(a)
# print(a)