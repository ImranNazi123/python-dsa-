n=3
ans=""
l=""

def noTwoHead(n,ans,l):
     # base case 
    if n==0:
        print(ans)
        return
    elif ans.endswith("HH"):
        return 0
    else:
        if l!="H":
            noTwoHead(n-1,ans+"H","H")
           
        noTwoHead(n-1,ans+"T","T")


noTwoHead(n,ans,l)



def ct(n,ans):
    # base case 
    if n==0:
        print(ans)
        return
    else:
        
        ct(n-1,ans+"H")
        ct(n-1,ans+"T")
# ct(n,ans)

