list_a=[1,2,3]
list_b=[4,5,6]

list_c=[]

list_lenght=len(list_a)

for i in range(list_lenght):
    print("i=", i)
    value_from_a=list_a[i]
    value_from_b=list_b[i]
    result=value_from_a+value_from_b
    list_c.append(result)
    print(list_c)