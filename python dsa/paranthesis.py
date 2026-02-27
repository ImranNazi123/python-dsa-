n=3
ans=""
close=0
open=0
l=[]
def para(n,open,close,ans,l):
    # base case
    if open==n and close==n:
        print(ans)
        l.append(ans)

    else:
        if open<n:
            para(n,open+1,close,ans+"(",l)
            # l.append(ans)
        
        if close<open:
            para(n,open,close+1,ans+")",l)
            # l.append(ans)


para(n,open,close,ans,l)
print(l)


