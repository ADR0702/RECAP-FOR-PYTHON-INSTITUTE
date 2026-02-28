sales = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

total=0
sold_item=0
most_sold=""


for item, amount in sales.items():
    total+=amount
    if amount > sold_item:
        sold_item=amount
        most_sold=item
    
print(f"the total amount of products sold are {total}")
print(f"the most sold item was {most_sold}")


team_a = ["ana", "ion", "maria", "paul", "ana"]
team_b = ["ion", "alex", "paul", "george"]

team_a=set(team_a)
team_b=set(team_b)

print(team_a | team_b)
print(team_a & team_b)
print(team_a - team_b)

nums = [12, 5, 7, 3, 9, 1]
minimum=nums[0]
for no in nums:
    if no < minimum:
        minimum=no

print(minimum)



numbers = [2, 4, 7, 9, 10, 13, 16]
odd=[]
even=[]

for no in numbers:
    if no % 2 == 0:
        odd.append(no)
    else:
        even.append(no)

print(odd)
print(even)

text = "ana are mere ana are pere mere"
text=text.split()
most_used={}
count=0

for word in text:
    count+=1
    if word in most_used:
        most_used[word]+=1
    else:
        most_used[word]=1

print(most_used)


