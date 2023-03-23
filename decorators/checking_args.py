from functools import wraps


# def prohibit_kwargs(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError('kwargs are prohibited')
#         return func(*args, **kwargs)
#
#     return wrapper()
#
#
# @prohibit_kwargs
# def print_hello(name):
#     print(f'Hello, {name}')
#
#
# print_hello(name='Jack')


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return func(*args, **kwargs)
        elif len(kwargs) < 3:
            return func(*args, **kwargs)
        else:
            raise ValueError('Function must have less than 3 arguments!')

    return wrapper


@prohibit_more_than_2_args
def some_func(a, b, c):
    return 'Foo'


print(some_func(a=1, b=2, c=3))
