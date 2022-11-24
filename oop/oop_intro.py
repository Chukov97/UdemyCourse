class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car('Mazda CX7', 'black', 2007, True)
print(mazda_car.wheels_number)
print(Car.wheels_number)


class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post_about_politicians = BlogPost('John', 'I like politicians', 10)
post_about_cats = BlogPost('Jane', 'I like cats', 0)

post_about_cats.number_of_likes = 50

print(post_about_politicians.number_of_likes)
print(post_about_cats.number_of_likes)
