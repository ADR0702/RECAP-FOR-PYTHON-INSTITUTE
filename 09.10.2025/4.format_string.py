name=input("please add your name\n")
city=input("please add your current city\n")
age=input("please add your age\n")

print("My name is " + name +  " i live in the city of " + city + " and i'm  " + age + " years old." )
print(f"My name is {name} i live in the city of {city} and i'm  {age} years old.")
print("My name is {n} i live in the city of {c} and i'm {a} years old.".format(n=name, c=city, a=age))