a=[5,1,3,4,2]



def sort(a):
    # loop..
    # 0-4
    for i in range (len(a)):
        swap=0
        # 0-3
        for j in range(len(a)-1):
            # print(a[j], end=" ")
            if a[j]>a[j+1]:
                # swap...
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
            

            
            swap+=1
        
        if swap==0:
            break

        print(a)


            



sort(a)

# print(a)