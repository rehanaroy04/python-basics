def frequency_of_elements(arr):
    freq = {}
    for element in arr:
        freq[element] = freq.get(element, 0) + 1
    return freq

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

numbers = [1, 2, 3, 2, 1, 3, 1, 4, 5, 4, 4, 2]
print("Frequency:", frequency_of_elements(numbers))

dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'d': 4, 'e': 5, 'f': 6}
print("Merged:", merge_dicts(dict_a, dict_b))