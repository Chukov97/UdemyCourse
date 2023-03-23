from functools import wraps


# def check_if_first_arg_is(val):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != val:
#                 print(f'first arg has to be {val}')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return inner_dec
#
#
# @check_if_first_arg_is('red')
# def print_rainbow_colors(*colors):
#     print(colors)
#
#
# @check_if_first_arg_is(7)
# def mult_seven(a, b):
#     return a * b
#
#
# print_rainbow_colors('black', 'red', 'green', 'blue', 'indigo')
# print(mult_seven(8, 3))

def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args)

        return wrapper

    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hello', '3')
