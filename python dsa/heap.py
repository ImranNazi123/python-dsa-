def arr3():
    # print no. from 1-11
    x=[i for i in range (1,6)]
    # print(x[9:7:-1]), to reverse no
    # split array list 
    # print(x[6:2:-1])
    print(x[::-2])




def test():
    for i in range(10,5,-1):
        print(i)
        # print no , in descending order...




def arr2():
    a=[21,23,45]
    b=[i for i in a]
    print(b)



def listComprehension():
    n=int(input())
    a=[int(input() ) for i in range(n)]
    # a=[i for i in range (n)]
    # prints all index no. only
    print(a) 




def arr1(a):
    n=int(input())
    for i in range (n):
        # print(i), by default i =0 ; value of i
        x=int(input())
        a.append(x)

    print(a)
    
# listComprehension()
# arr1(a)

# arr2()

# test()
arr3()