class Swimmable:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can swim')

    def swim(self):
        print('i\'m swimming')


class Walkable:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can walk')

    def walk(self):
        print('i\'m walking')


class Flyable:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can fly')

    def fly(self):
        print('i\'m flying')


class GameCharacter(Swimmable, Walkable, Flyable):

    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f'Hello! My name is {self.name}')


james = GameCharacter('James')
james.greeting()

print(isinstance(james, Walkable))
print(isinstance(james, Swimmable))
print(isinstance(james, Flyable))
print(isinstance(james, GameCharacter))
print(isinstance(james, object))

