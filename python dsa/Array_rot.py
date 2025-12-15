a=[1,2,3,4,5,6]

def rotate_2(a,k):
    # a=a[len(a)-k:len(a):]
    a=a[len(a)-k:]+a[0:len(a)-k:]
    # above swap .....
    print(a)

def rotate_1(a):
    t=a.pop()
    a.insert(0,t)

def rotate(a,k):
    k=k%len(a)
    # fun.. to rotate as per k times ...
    for i in range(k):
        rotate_1(a)

# rotate(a,3)
rotate_2(a,3) 

# a=a[len(a)-3:]
# print(a)
# print(len(a))


# print(a)
    




