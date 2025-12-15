a=0
b=1
str=1
n=5
r=1

while r<=n:
    # star
    i=1
    while i<=str:
        print(a,end="\t")
        i+=1
        c=a+b
        a=b
        b=c 
    
    # upd....
    str+=1
    r+=1
    
    print()

