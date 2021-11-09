#  Lists in lists
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[0][0])
print(lst[1][0])
lst[0] = [10, 11, 12]
print(lst)
print(lst[0][0])
lst[1][2] = 15
print(lst)
my_array = [[[111, 112, 113], [121, 122, 123], [131, 132, 133],\
             [211, 212, 213], [221, 222, 223],[231, 232, 233],\
             [311, 312, 313], [321, 322, 323], [331, 332, 333]]]
print(my_array)
print(my_array[1][0][2])