rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 45, 567, 234]
text_tuple = ('afd', 'dfg', 'ref')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')

set_from_list.add(777)
set_from_tuple.add('hello')

x = set_from_list.pop()
y = set_from_tuple.remove('ref')
set_from_list.discard(777)
set_from_list.discard(777)
# set_from_list.clear()

print(set_from_list)
print(set_from_tuple)
print(x, y)

letters_set = set('Создайте множество при помощи функции set() '
                  'из текста, чтобы получить уникальные символы, '
                  'содержащиеся в тексте.')
print(letters_set)
print(type(letters_set))
