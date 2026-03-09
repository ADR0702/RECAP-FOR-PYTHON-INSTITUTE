def show_user(**data):
    for key, value in data.items():
        print(key, value)

show_user(name="Ana", age=22)


def count_items(**data):
    return len(data)

print(count_items(a=1,b=2,c=3))


def sum_values(**data):
    final_sum=0
    for v in data.values():
        final_sum+=v
    return final_sum

print(sum_values(a=3,b=4,c=5))

def largest_value(**data):
    largest=0
    for v in data.values():
        if v > largest:
            largest=v
    return largest

print(largest_value(a=3,b=9,c=5))


def print_keys(**data):
    for key in data:
        print(key)
    
print_keys(name="Ana", age=22, city="Cluj")

