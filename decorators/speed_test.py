from time import time
from functools import wraps


def speed_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'Time of code execution {end_time - start_time}')
        return result

    return wrapper


@speed_test
def sum_with_list():
    return sum([number for number in range(10000000)])


@speed_test
def sum_with_gen():
    return sum(number for number in range(10000000))


print(sum_with_list())
sum_with_gen()
