# pattern 
n=int(input())

def pattern1(n):
    val=n

    for i in range(1,n,):
        # print vertically....
        for l in range(1,n,):
            print(l)
            print(end=" ")

        

pattern1(n)




























# row=1
# str=1
# spc=2*n-3 

# while row<=n:
#     # str
#     i=1
    
#     while i<=str:
#         print(i,end="\t")
#         i+=1
#         # cval=i
#     # space
#     j=1
#     while j<=spc:
#         print("  ",end="\t")
#         j+=1
#     # str
    
#     i=1
#     # if str==n:
#     #     i=2
#     cval=str
#     if str==n:
#         cval=str-1

#     while cval!=0:
        
#         print(cval,end="\t")
#         cval-=1

#     str+=1
#     row+=1
#     spc-=2
#     print("   ")

    
    
    















# # dec-oct
# n=20
# ans=0
# mul=1
# while n!=0:
#     rem=n%8

#     ans+=mul*rem

#     mul*=10
#     n//=8

# print(ans)






# # dec to binary
# n=57
# ans=0
# mul=1
# while n!=0:
#     rem=n%2

#     ans+=mul*rem

#     mul*=10
#     n//=2

# print(ans)















# # binary to decimal
# # n=111001
# n=int(input())

# ans=0
# val=1
# while n!=0:
#     # last digit...
#     rem=n%10

#     ans+=rem*val

#     val*=2
#     n//=10

# print(ans)

























# # # pattern-2
# # n=int(input())
# # row=1
# # star=n
# # val=1
# # while row<=n:
# #     # star
# #     i=1
# #     while i<=val:
# #         print(star,end=" ")
# #         i+=1
    
# #     print(" ")
# #     star-=1
# #     row+=1
# #     val+=1






















# # # # pattern-1

# # # n=int(input(" "))
# # # star=n
# # # row=1

# # # while row<=n:
# # #     # star
# # #     i=1
# # #     while i<=star:
# # #         print("* ",end=" ")
# # #         i+=1
    
# # #     # next line...
# # #     print(" ")
# # #     row+=1


























# # # # # bin to decimal....
# # # # n=57
# # # # ans=0
# # # # mult=1
# # # # while n!=0:
# # # #     rem=n%2
# # # #     ans+=rem*mult

# # # #     mult*=10

# # # #     # reduce n ...
# # # #     n//=2

# # # # print(ans)
