a=[1,2,3,4]
# a=[-1,1,0,-3,3]
l=[]
# prod=1

# productExceptSelf_m2()-->to beat time complexity......
def productExceptSelf_m2(a):
    # left prod...
    l=[0 for i in range(len(a))]
    r=[0 for i in range(len(a))]
    # product...
    p=1

    # left...
    for i in range(len(a)):
        l[i]=p
        p*=a[i]
    
    # print(l)
    # right....
    p=1
    for i in range(len(a)-1,-1,-1):
        r[i]=p
        p*=a[i]
    
    # print(r)

    ans=[]
    for i in range(len(a)):
        ans.append(l[i]*r[i])
    
    return ans



def productExceptSelf(a,l):
    i=0
    # l=a
    
    while i<len(a):
        # prod...
        prod=1
        j=0
        while j<len(a):
            if j!=i:
                prod=prod*a[j]
            j+=1
        # l[i]=prod
        l.append(prod)
        # print(l)
        # prod=1
        i+=1
    return l

# x=productExceptSelf(a,l)
# l[3]=67
# print(x)
# print(a)
x=productExceptSelf_m2(a)
print(x)
# print(l)
