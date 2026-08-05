# n = 2 
a=[20,5,0,25,15,10]



# let first max elem be..
fmax=float('-inf')
# 2nd max elem be..
smax=float('-inf')
# 3rd...
tmax=float('-inf')


for i in a:
    if i>fmax:
        # temp.
        
        tmax=smax
        smax=fmax
        fmax=i

    elif i>smax:
        tmax=smax
        smax=i
    elif i>tmax:
        tmax=i


print(fmax)
print(smax)
print(tmax)















# print(1//2)












# for i in range(2, n-1):
#     if n % i == 0:
#         print("Composite")
#         break
# else:
#     print("Prime")
    
   
    















# for i in range(0,5):
#     print(i)
