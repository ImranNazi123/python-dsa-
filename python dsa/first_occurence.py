

# print(a)


def first_occur(a ,k):
    for i,num in enumerate(a):
        if num==k:
            return i

    return -1
        


# size..
n=int(input())
# key
k=int(input())
# array..
a=[int(input()) for i in range(n)]





print(first_occur(a,k))




