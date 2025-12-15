def pattern_1(n):
    # for i in range (0,n):
    #     print(i,end=" ")
    r=1
    str=n
    # loop
    # row
    while r<=n:
        i=1
        while i<=str:
            if i%2!=0 or r%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
            i+=1
        r+=1
        print()
                



pattern_1(5)



# o/p:
# 0 1 0 1 0 
# 0 0 0 0 0 
# 0 1 0 1 0 
# 0 0 0 0 0 
# 0 1 0 1 0 