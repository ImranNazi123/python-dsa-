a=[5,1,4,3,2]

# function to take array and last digit as input.....
def insertion(a,lst):
    t=a[lst]
    # loop in decreasing order...
    for i in range(lst-1,-1,-1):
        if a[i]>t:
            # swap
            a[i+1]=a[i]
        else:
            a[i+1]=t
            break

    else:
        a[0]=t
    

    


        




def swap(a):
    # loop
    # 0-a.length...ie.. [1-4]
    for i in range(1,len(a)):

        insertion(a,i)

swap(a)
print(a)