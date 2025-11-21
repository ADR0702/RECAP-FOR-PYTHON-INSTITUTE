def fun1(x):
    return x
def fun2(x):
    return x * 2
def fun3(x):
    return x+3
x=fun1(fun2(fun3(1)))
print(x)