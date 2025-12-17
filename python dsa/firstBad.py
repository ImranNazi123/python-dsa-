n=5
bad=4
# ans=0
def firstBadVersion(n,bad):
    si=1
    ei=n
    ans=0

    while si<=ei:
        mid=int((si+ei)//2)
        if mid==bad:
            ans=mid
            # to check if theres bad left ...
            ei=mid-1
        
        elif mid>bad:
            ei=mid-1
        
        else:
            si=mid+1
    return ans

y=firstBadVersion(n,bad)
print(y)
    





