class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'Person object with name {self.firstname} is deleted from memory')

    def __add__(self, other):
        return self.age + other.age


jack = Person('Jack', 'White', 27)
jane = Person('Jane', 'Air', 23)

print(jack)
print(len(jack))
del (jack)


class Chain:

    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return f'Chain with {self.number_of_items} items'

    def __len__(self):
        return self.number_of_items


chain = Chain(25)
print(chain)
print(len(chain))
