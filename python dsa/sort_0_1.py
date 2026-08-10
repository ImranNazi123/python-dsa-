# a=map(int,input().split())
n=int(input())
a=[int(input()) for i in range(n)]

def sort(a):

    return sorted(a)

x=sort(a)

for i in x:
    print(i, end=" ")

# i/p:1 1 1 0 0
# o/p:0 0 1 1 1

