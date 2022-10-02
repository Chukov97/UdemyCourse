tuple_1 = (1, 2, 3)
tuple_2 = ('one', 'two')
tuple_3 = (2, 3.45, 'three')

print(tuple_1)
print(tuple_2)
print(tuple_3[2])

person_tuple = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple

print(first_name, last_name, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(5))

greetings_tuple = ('hello', 'hi', 'hey', 'hi')
print(greetings_tuple.count('hola'))

print(t1.index(1))
print(greetings_tuple.index('hi'))
