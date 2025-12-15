a=[1,2,3,4,5,6,7,8]
b=[1,2,3,3,3,5,5,7,7]
fnd=int(input())

def binarySearch(a,ele):

    si=0
    ei=len(a)-1
    # loop
    while si<=ei:
        # mid index value: 
        mid=int((si+ei)/2)
        if a[mid]==ele:
            return mid
        
        elif a[mid]>ele:
        
            ei=mid-1
        
        else :
            si=mid+1
        
    # return -ve val , if nothing is present......
     
    return -1

# function to check first occurance no.... 
# lower bound function...--ve
# upper bound function...++ve (just right of first ocuurance of finding element ...)
def FirstOccurance(b,ele):
    si=0
    ei=len(a)-1
    # ans=-1
    # loop
    while si<=ei:
        # mid index value: 
        mid=int((si+ei)/2)
        if b[mid]==ele:
            ans=mid

            ei=mid-1
        
        elif b[mid]>ele:
        
            ei=mid-1
        
        else :
            si=mid+1
        
    # return -ve val , if nothing is present......
     
    return ans


# y=binarySearch(a,fnd)
y=FirstOccurance(b,fnd)
print("ele is in index: ",y)




    