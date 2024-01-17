# 1.1

def find_max_value(n_list):
    return max(n_list)

num_list = [15, 7, 22, 45, 18, 32]
max_value = find_max_value(num_list)
print("Maximum value in the list:", max_value)

# 1.2

# append: Adding an element to the end of the list
aei_list = [1, 2, 3]
aei_list.append(4)
print("aie_list after append:", aei_list)

# Extend: Adding elements from an iterable to the end of the list
aei_list.extend([5, 6, 7])
print("aie_list after extend:", aei_list)

# Insert: Inserting an element at a specific index in the list(we should mention the index)
aei_list.insert(1, 8)
print("aie_list after insert:", aei_list)

# 1.3

def remove_duplicates(n_lst):
    return list(set(n_lst))

# Example usage:
first_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(first_list)
print("List with duplicates:", first_list)
print("List without duplicates:", unique_list)

# 1.4

def check_sorted_ascending(n_list):
    return all(n_list[i] <= n_list[i + 1] for i in range(len(n_list) - 1))

sorted_list = [1, 3, 5, 7, 9]
unsorted_list = [4, 2, 8, 6, 10]

print("Is sorted (ascending):", check_sorted_ascending(sorted_list))
print("Is sorted (ascending):", check_sorted_ascending(unsorted_list))

# 1.5

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements_list = find_common_elements(list1, list2)
print("Common elements between two lists:", common_elements_list)
