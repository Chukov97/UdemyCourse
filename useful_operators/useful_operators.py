for x in range(10):
    print(x)
print(range(8))
print(list(range(5)))

letter_index = 0
my_string = 'dsfjhgjfd'
for letter in my_string:
    print(letter + ' is at index ' + str(letter_index))
    letter_index = letter_index + 1

my_string = 'dsfjhgjfd'
for item in enumerate(my_string):
    print(item)

print('a' in 'Jack')
print('x' in 'Jack')
print(str(1) in 'Jack')
print('1' in 'Jack')

letter_list = ['a', 'b', 'c', True]
print('a' in letter_list)
print(1 in letter_list)

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(1 in dict_1)
print(1 in dict_1.keys())
print(4 in dict_1.keys())
print('c' in dict_1.values())
print('x' in dict_1.values())

print(min(1, 3, 56, 4))
print(max(1, 3, 56, 4))
my_list = [1, 3, 56, 4]
print(min(my_list))
print(max('Hello'))
for letter in 'Hello':
    print(ord(letter))

from random import shuffle

my_list = [1, 3, 56, 4]
shuffle(my_list)
print(my_list)

from random import randint

print(randint(1, 10))
