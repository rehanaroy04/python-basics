def tuple_to_list(tpl):
    return list(tpl)

def list_to_tuple(lst):
    return tuple(lst)

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Converted to list:", tuple_to_list(my_tuple))

my_list = [10, 20, 30, 40, 50]
print("List:", my_list)
print("Converted to tuple:", list_to_tuple(my_list))

my_tuple2 = ('a', 'b', 'c')
print("Tuple to list:", list(my_tuple2))

my_list2 = ['x', 'y', 'z']
print("List to tuple:", tuple(my_list2))