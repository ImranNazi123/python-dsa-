n=int(input())
k=int(input())
a=[int(input()) for i in range(n)]

def last_occur(a,k):

    for i in range(len(a)-1,-1,-1):
        if a[i]==k:
            return i 

    return -1


print(last_occur(a,k))