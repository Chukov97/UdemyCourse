# Inheritance

class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print("Car is created")

    def drive(self, city):
        print(f'{self.name} is driving to {city}')

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):
    wheels_number = 6

    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('Truck is created')

    def drive(self, city):
        print(f'Truck {self.name} is driving to {city}')

    def load_cargo(self, weight):
        print(f'The cargo is loaded. Weight is {weight} kg')


man_truck = Truck('Man', 'black', 2019, True)

man_truck.drive('New York')
print(man_truck.wheels_number)
man_truck.load_cargo(2000)


# Polymorphism

class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying woof')


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying meow')


class Mouse:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying pee-pee-pee')


class Fish:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying nothing')


spice = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')
pet_list = [spice, tom, jerry]

for pet in pet_list:
    pet.speak()


def pet_voice(pet):
    pet.speak()


pet_voice(spice)
pet_voice(tom)

freddy = Fish('Freddy')
pet_voice(freddy)


class GameCharacter:

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print(f'Hi, my name is {self.name}')


class Villain(GameCharacter):

    def speak(self):
        print(f'Hi, my name is {self.name} and i will kill you')

    def kill(self, other):
        other.health = 0
        print(f'Bang-bang, now you\'re dead')


james = GameCharacter('James', 100, 1)
jim = Villain('Jim', 100, 2)

james.speak()
jim.speak()
print(james.health)
jim.kill(james)
print(james.health)
