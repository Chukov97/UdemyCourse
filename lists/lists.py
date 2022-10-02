number_list = [32, 21, 48, 34.56]
print(number_list)
some_list = [12, 34.56, 'Hello']
print(some_list)
print(len(some_list))
print(some_list[1])
another_list = some_list[:2]
print(another_list)
some_list[2] = 'hi'
print(some_list)
new_list = some_list + another_list
print(new_list)

# adding items
new_list.append('new item')
new_list.insert(0, 'start')

# removing items
new_list.pop()
new_list.remove(12)

print(new_list)

number_list_new = [43, 54, 3, -54, 23.2]
letter_list = ['s', 'w', 'r', 'l', 'e']

number_list_new.sort()
letter_list.sort()

print(number_list_new)
print(letter_list)

number_list_new.reverse()
letter_list.reverse()
number_list_new.append(letter_list)

print(number_list_new)
print(letter_list)
