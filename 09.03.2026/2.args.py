

def multiply_all(*numbers):
    prod=1
    for n in numbers:
        prod*=n
    return prod

print(multiply_all(2,3))
print(multiply_all(2,3,4))


def count_positive(*numbers):
    count=0
    for n in numbers:
        if n > 0:
            count+=1
    return count

print(count_positive(1,-2,3,4,-1))

def largest(*numbers):
    largest_no=numbers[0]
    for n in numbers:
        if n > largest_no:
            largest_no=n
    return largest_no

print(largest(3,7,2,9,5))

def test(*args):
    print(args)

test(1,2,3)


