height = [1,8,6,2,5,4,8,3,7]

def maximum_count(height):
    n=len(height)
    i=0
    j=n-1
    max_so_far=0

    # loop
    while i<j:

        # height.to trap water..
        h=min(height[i],height[j])
        # width
        w=j-i
        # area
        a=w*h
        # max_area..
        max_so_far=max(max_so_far,a)

        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_so_far

print(maximum_count(height))
        


    