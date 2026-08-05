# using dictionary , default , 

from collections import *

def is_anagram(s1,s2):
    f1=Counter(s1)
    print("f1= ",f1)
    f2=Counter(s2)
    print("f2= ",f2)

    return f1==f2


s1=input()
s2=input()

print(is_anagram(s1,s2))

