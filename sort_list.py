def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(sort_list(user_list))