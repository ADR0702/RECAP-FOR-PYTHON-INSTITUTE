a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

a=set(a)
b=set(b)


print(a | b)
print(a&b)
print(a-b)

group1 = ["ana", "ion", "maria", "paul"]
group2 = ["ion", "paul", "george", "alex"]

group1=set(group1)
group2=set(group2)

print(group1-group2)
print(group2-group1)
print(group1 | group2)


online_users = ["ana", "ion", "maria", "paul", "ion"]
subscribed_users = ["ion", "george", "ana", "alex"]

online_users=set(online_users)
subscribed_users=set(subscribed_users)

print(online_users|subscribed_users)
print(subscribed_users&online_users)
print(subscribed_users^online_users)

numbers = [4, 7, 2, 7, 9, 2, 1, 4, 10]
numbers=set(numbers)
print(numbers)

max_number=0
for no in numbers:
    if no > max_number:
        max_number=no
print(max_number)