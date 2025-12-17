n=5

def pattern(n):
    r=1
    str=1
    l=1
    # ans=l
    while r<=n:
        # str
        i=1
        ans=l
        while i<=str:
            # i+=1
            print(ans,end=" ")
            i+=1
            ans+=1
        str+=1
        r+=1
        l+=1

        print()


pattern(n)
    
# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7 
# 5 6 7 8 9 
