def my_func(a, b):
    return sum((a, b))


print(my_func(40, 60))


def a_func(*args):
    return sum(args)


print(a_func(2, 3, 6, 8, 9))


def my_func(*args):
    return sum(args) * 0.05


print(my_func(40, 60))


def my_func(*args):
    for item in args:
        print(item)


my_func(40, 60, 30, 50)


def names(*args):
    for name in args:
        print(name)


names('chris', 'benny', 'jeff')


def names(a, b):
    return a, b


print(names('jacob', 'larry'))


def cars(**kwargs):
    print(kwargs)
    if "car" in kwargs:
        print("my favorite car is {}".format(kwargs['car']))
    else:
        print("there is not car here")


cars(car="honda")

# check for even numbers using For loop

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")

# get the sum of every number my_list

list_sum = 0

for num in my_list:
    list_sum = list_sum + num

print(list_sum)

# create a string and and iterate through string

my_string = "Hello World"

for letter in my_string:
    print(letter)


tuple_num = (1, 2, 3)

for item in tuple_num:
    print(item)

new_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

len(new_list)

for item in new_list:
    print(item)

# tuple unpacking
# prints out each char at index (a)
for a, b in new_list:
    print(a)

# prints out each char at index (b)
for a, b in new_list:
    print(b)

old_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for item in old_list:
    print(item)

# tuple unpacking the variable old_list
# given each index
for a, b, c in old_list:
    print(a, b, c)

# prints out each char at index c
for a, b, c in old_list:
    print(c)


# create a dictionary and iterate through each key

dict = {"k1": 1, "k2": 2, "k3": 3}

# by default when you iterate through a dictionary, you iterate through each KEY
for item in dict:
    print(item)

# return items()

for item in dict.items():
    print(item)

# return each key

for item in dict.keys():
    print(item)


# return each value

for item in dict.values():
    print(item)

# tuple unpacking with DICTIONARY
for key, value in dict.items():
    print(value)


for key, value in dict.items():
    print(key)