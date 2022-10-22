greeting = 'hello!'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)

letter_list = [letter for letter in greeting]
print(letter_list)

number_list = [number for number in '0123456789']
print(number_list)
number_list_1 = [num for num in range(0, 10)]
print(number_list_1)
number_list_2 = [num ** 2 for num in range(0, 10)]
print(number_list_2)
number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(0, 10)]
print(number_list_3)

number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
new_list = [number for number in number_list if number > 0]
print(new_list)
new_list = [number ** 3 / 2 for number in number_list if number > 0]
print(new_list)
new_list_1 = ['+' if number > 0 else '-' for number in number_list]
new_list_1 = ['+' if number > 0 else '-' if number < 0
else 'zero' for number in number_list]
print(new_list_1)

# With List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = [greeting[1] for greeting in greetings]
print(letter_list)

# Without List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = []
for greeting in greetings:
    letter_list.append(greeting[1])
print(letter_list)

# With List Comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [digit for digit in digits if digit % 2 == 1]
print(odd_numbers)

# Without List Comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
for digit in digits:
    if digit % 2 == 1:
        odd_numbers.append(digit)
print(odd_numbers)
