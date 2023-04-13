# lorem_ipsum_text = open('sample.txt')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()

# lorem_ipsum_text = open('sample.txt')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()

# with open('sample.txt') as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     while line:
#         print(line, end='')
#         line = lorem_ipsum_text.readline()

# with open('sample.txt', 'r') as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')


colors_list = ['red', 'orange', 'green', 'blue', 'white', 'black']
with open('color.txt', 'w') as colors:
    for color in colors_list:
        print(color, file=colors)

colors_list = []
with open('color.txt', 'r') as colors:
    for color in colors:
        colors_list.append(color)

print(colors_list)
