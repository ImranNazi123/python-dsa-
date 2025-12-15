a=[5,3,2,1,4]

def Sort(a):
    for i in range (len(a)):
        # print(a[i],end=" ")
        min_i=i
        for j in range(i+1,len(a)):
            if a[min_i]>a[j]:
                min_i=j
        # swap with min val
        t=a[i]
        a[i]=a[min_i]
        a[min_i]=t



            


Sort(a)
print(a)