n=0
# ncr=1
N=5

while n<N:
    r=1
    ncr=1
    # str
    while r<=n+1:
        print(ncr,end=" ")
        # upd...
        ncr=int((((n-r+1)/r)*ncr))
        r+=1
    
    # upd...
    print()
    n+=1


# / is float division....
# // is int division
























# N=5
# n=0

# # 0-4
# while n<N:

#     # start.....rows...
#     ncr=1
#     r=1


#     while r<=n+1:
#         print(ncr,end=" ")
        
#         # upd...
#         ncr=int(((n-r+1)/r)*ncr)
#         r+=1
    
#     # upd....
#     n+=1
#     print()





# print(23,56)