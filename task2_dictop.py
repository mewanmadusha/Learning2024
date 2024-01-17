# 2.1

def find_average_score(grades):
    return sum(grades.values()) / len(grades)

student_grades = {'Math': 85, 'English': 90, 'Science': 78, 'History': 92}

avg_score = find_average_score(student_grades)
print("Average score:", avg_score)

# 2.2

def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage:
dict1 = {'a': 'pothumulla', 'b': 'kankanamge'}
dict2 = {'b': 'mewan', 'c': 'madusha'}
merged_dict = merge_dictionaries(dict1, dict2)
# merged_dict = merge_dictionaries(dict2, dict1)
print("Merged dictionary:", merged_dict)

# 2.3

def top_n_keys(dictionary, n):
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    return sorted_keys[:n]

n=2
grades = {'Math': 85, 'English': 90, 'Science': 78, 'History': 92}
top_keys = top_n_keys(grades, n)
print(f"Top {n} keys with highest values: {top_keys}")

# 2.4
def sort_dict_by_values(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict


unsorted_dict = {'b': 3, 'a': 1, 'c': 4}
sorted_dict = sort_dict_by_values(unsorted_dict)
print("Sorted dictionary by values:", sorted_dict)