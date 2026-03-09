def addfive(number):
    return number+5

print(addfive(10))

def multiply(a, b):
    return a * b

print(multiply(35,250))

def is_positive(n):
    if n >= 0:
        return True
    else:
        return False
    
print(is_positive(7))
print(is_positive(-2))

def double(x):
    return x * 2

def square(x):
    return x ** 2


print(square(double(3)))

def bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a, b
    
print(bigger(8, 3))
print(bigger(2, 10))

def sum_of_squares(a, b):
    return a **2 + b**2


print(sum_of_squares(3,4))

def increment(number, step=1):
    print(number + step)

increment(10)     
increment(10,5)  


