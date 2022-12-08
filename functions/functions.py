def print_greeting():
    """
    print 'Hello!'
    :return: None
    """
    print('Hello!')


print_greeting()
help(print_greeting)


def print_greeting_with_name(name='Name'):
    """
    :param name
    :return: None
    """
    print(f'Hello, {name}!')


print_greeting_with_name('Alex')
help(print_greeting_with_name)


def sum_of_two(a=0, b=0):
    """

    :param a:
    :param b:
    :return: Sum a and b
    """
    return a + b


x = sum_of_two(4, 5)
print(x)


def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    return False


print(is_hello_in_text('hell'))


def is_string_in_text(string, text):
    return string in text


print(is_string_in_text('aaa', 'Kaaa'))


def cat_voice():
    print('Meow!')


cat_voice()


def dog_voice():
    print('Woof!')


dog_voice()


def cat_voice():
    return 'Meow!'


def dog_voice():
    return 'Woof!'


print(cat_voice())
print(cat_voice())
print(dog_voice())
print(dog_voice())


def get_voice(text):
    return f'{text}!'


print(get_voice('Hello'))


def generation(a, b):
    new_list = []
    for i in range(a, b + 1):
        if i % 2 == 1:
            new_list.append(i)
    return new_list


print(generation(2, 11))


def generation_list_comp(a, b):
    return [x for x in range(a, b + 1) if x % 2 == 1]


print(generation_list_comp(2, 11))
