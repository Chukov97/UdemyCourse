nested_list = [[1, 2, 4], [3, 5, 6, 4, 5], [7, 8, 9]]

print(nested_list)
print(len(nested_list))
print(len(nested_list[1]))
print(nested_list[1][2])

for inner_list in nested_list:
    print(inner_list)

for inner_list in nested_list:
    for number in inner_list:
        print(number)

[[print(number) for number in inner_list] for inner_list in nested_list]
