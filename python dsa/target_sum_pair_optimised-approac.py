# optimised sol...
# time:0(n), both B.C AND W.C
# 2 pointer approach...
n,t=map(int,input().split())
# array..
a=[10,20,40,50]

def target_sum_pair_count(n,a,t):
    i=0
    j=n-1
    count=0
    # loop
    while i<j:
        # cond..
        if a[i]+a[j]<t:
            i+=1
        elif a[i]+a[j]>t:
            j-=1
        else:
            count+=1
            i+=1
            j-=1
    if count>0:
        return count
    else:
        return -1

print(target_sum_pair_count(n,a,t))    
        






