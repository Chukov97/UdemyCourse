def ten_percent_of_product(x, y):
    return (x * y) * 0.1


print(ten_percent_of_product(10, 20))


def ten_percent_of_product_with_args(percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent


print(ten_percent_of_product_with_args(20, 100, 10))


def func_with_kwargs(**kwargs):
    print(kwargs)


def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello! Nice to meet you, {}'.format(kwargs['name']))
    else:
        print('Hello! What is your name?')


hello_with_kwargs(gender='male', age=25, name='Jack')


def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
    else:
        print('{}! What is your name?'.format(greeting))


hello_with_greeting_and_kwargs('Hi', gender='male', age=25, name='Jack')


def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')


def is_here_cat(*args):
    args_in_lower_case = [str(argument).lower() for argument in list(args)]
    return 'cat' in args_in_lower_case


def is_item_here(item, *args):
    return item in args


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))
