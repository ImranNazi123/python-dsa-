# to print 3 largest elements in array..
# size of an array..
n=int(input())
# array..
a=[int(input()) for i in range(n)]


# let first max elem be..
fmax=float('-inf')
# 2nd max elem be..
smax=float('-inf')
# 3rd...
tmax=float('-inf')

# for loop...
for num in a:
    if num>fmax:
        # temp.
        
        tmax=smax
        smax=fmax
        fmax=num

    elif num>smax:
        tmax=smax
        smax=num
    elif num>tmax:
        tmax=num

print(fmax)
print(smax)
print(tmax)

# 20
# 5
# 0
# 25
# 15
# 10

# o/p: 25 , 20, 15


