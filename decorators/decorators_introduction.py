# def decorator_func(orig_func):
#     def wrap_func():
#         print('Some text before')
#         orig_func()
#         print('Some text after')
#
#     return wrap_func
#
#
# @decorator_func
# def simple_func():
#     print('Simple func code')
#
#
# simple_func()

def make_compliment(func):
    def wrapper(*args):
        print('Nice to meet you')
        func(*args)
        print('Some text...')

    return wrapper


@make_compliment
def ask_name():
    print('What is your name?')


ask_name()
