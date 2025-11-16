a=[1,2,3]
b=[4,5,6]

print(type(a), type(a[0]))


print("Searching through index:")

c=[]
print("c=", c)

for i in range(len(a)):
    print("i=", i)
    c.append(a[i]+b[i])
    print("c=", c)