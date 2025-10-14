product1=int(input("please add the price of the first product:\n"))
product2=int(input("please add the price of the second product:\n"))
product3=int(input("please add the price of the third product:\n"))

total=product1+product2+product3
average_price=total/3
remainder=total%2

print(f"The total price of the products is:{total}")
print(f"The average price of the products is: {average_price}")
print(f"The remainder of the price is: {remainder}")