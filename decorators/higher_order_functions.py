# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# print(product(4, square))
# print(product(4, cube))

# def my_func(a, b, func):
#     result = func([a, b])
#     return result
#
#
# print(my_func(2, 3, sum))

from random import choice


#
#
# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'blue')
#         color = choice(colors)
#         return color
#
#     result = get_color() + ' ' + thing
#     return result
#
#
# print(colorize('apple'))


# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'blue')
#         color = choice(colors)
#         return color
#
#     return get_color()
#
#
# first_color = make_color()
# print(first_color)

def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'blue')
        color = choice(colors)
        return color

    result = get_color() + ' ' + thing
    return result
