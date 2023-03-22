from functools import wraps


def print_func_data(func):
    """

    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'You are using  {func.__name__}')
        print(f'Func docs {func.__doc__}')
        return func(*args, **kwargs)

    return wrapper


@print_func_data
def squares_sum(a, b):
    """

    :param a:
    :param b:
    :return: sum of squares
    """
    return a * a + b * b


print(squares_sum(3, 4))
print(squares_sum.__name__)
print(squares_sum.__doc__)
