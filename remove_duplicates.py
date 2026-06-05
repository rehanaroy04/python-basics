def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(remove_duplicates(user_list))