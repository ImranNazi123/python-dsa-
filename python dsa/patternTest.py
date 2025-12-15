n=int(input())

def pattern_2(n):
    # i=0
    r=1
    str=1
    while r<=n:
        # str
        i=1
        while i<=str:
            if r%2!=0 and i%2!=0:
                print(1,end=" ")
            else:
                print(0,end=" ")
            i+=1
        
        # updt...
        r+=1
        str+=1
        print()




def pattern_1(n):
    str=1
    str2=1
    r=1
    while r<=n:
        i=1

        # str print...
        while i<=str:
            print(str2,end=" ")
            i+=1
        
        r+=1
        str2+=1
        str+=1
        print()



# pattern_1(n)

pattern_2(n)