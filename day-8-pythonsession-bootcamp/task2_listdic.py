# 3.1
def combine_twolists_to_dict(keys, values):
    combined_dict = dict(zip(keys, values))
    return combined_dict

keys_list = ['a', 'b', 'c']
values_list = ['mew', 'madusha', 'pothumulla']

result_dict = combine_twolists_to_dict(keys_list, values_list)
print("Dictionary:", result_dict)

# 3.2


def get_most_frequent_element(lst):
    most_frequent_element = max(set(lst), key=lst.count)
    count = lst.count(most_frequent_element)
    return most_frequent_element, count

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

most_frequent, count = get_most_frequent_element(my_list)
print(f"Most frequent element: {most_frequent}, Count: {count}")

# 3.3

def calculate_total_sum_of_values(list_of_dicts):
    result_dict = {}
    for d in list_of_dicts:
        for key, value in d.items():
            result_dict[key] = result_dict.get(key, 0) + value
    return result_dict

list_of_dicts = [{'a': 10, 'b': 20}, {'a': 5, 'c': 15}, {'d': 6, 'c': 15}]

sum_of_values = calculate_total_sum_of_values(list_of_dicts)
print("Total sum of values for each key:", sum_of_values)

# 3.4

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = flatten_nested_list(nested_list)
print(flattened_list)


# 3.5
def find_first_occurrence_index(lst, element):
    try:
        index = lst.index(element)
        return index
    except ValueError:
        return "Unable to find element"  # Return None if the element is not found

my_list = [10, 20, 30, 40, 20, 50]

element_to_find = 20
index = find_first_occurrence_index(my_list, element_to_find)
print(f"Index of the first occurrence of {element_to_find}: {index}")