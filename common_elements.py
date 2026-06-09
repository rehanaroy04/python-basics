def common_elements(list1, list2):
    return list(set(list1) & set(list2))

list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]
print(common_elements(list_a, list_b))

list_c = ['apple', 'banana', 'orange', 'grape']
list_d = ['banana', 'kiwi', 'grape', 'mango']
print(common_elements(list_c, list_d))