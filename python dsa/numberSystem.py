#decimal to binary conversion.......
n=57
ans=0
i=0
mult=1
while n!=0:
# store reminder value.....
        
            rem=n%2
# to reduce n value to zero........

            n//=2
            # rem1*10^0+rem2*10^1.....
            ans+=mult*rem
            mult*=10

        

            
            


print(ans)
