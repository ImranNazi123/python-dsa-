# d=[4,3,2,1]
d=[9,9]
# d=[10]


# d[len(d)-1]=d[len(d)-1]+1
d=[int("".join(map(str,d)))+1]

d=[int(r) for num in d for r in str(num)]
print(d)
# print(type(d[0]))
# print(d[len(d)-1]=d[len(d)-1])


# l=[4,3,3]
# # convert list into string , then int ....
# r=[int(d) for num in l for d in str(num)]