# n=int(input())
# a=[int(input()) for i in range(n)]
a=[10,20,30,40,21]
# rotate arr..
r=3

def rotate(a,r):
    for j in range(r):
        temp=a[len(a)-1]
        for i in range(len(a)-1,0,-1):
            a[i]=a[i-1]

        a[0]=temp

rotate(a,r)
print(a)
    
    

