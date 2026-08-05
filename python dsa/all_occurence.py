n=int(input())
k=int(input())
a=[int(input()) for i in range(n)]

def all_occur(a,k):
    flag=False
    for i,num in enumerate(a):
        if num==k:
            flag=True
            print(i, end=" ")
            
    if flag==False:
        print(-1)


all_occur(a,k)