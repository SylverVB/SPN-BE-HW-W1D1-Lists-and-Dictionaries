import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

# Lesson 1: Assignment | Lists and Dictionaries

# ============ Advanced Operations on Python Lists ============

# Objective: Understand Python lists by exploring more complex operations, such as list comprehension, slicing, and sorting, and analyzing their time and space complexities.

# Problem Statement: Delve deeper into Python lists and master advanced operations. Implement various complex tasks using lists and analyze their efficiency in terms of time and space complexities.

# Task 1
# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.

def squares(n):
    return [num * num for num in range(1, n + 1)]

print(squares(5))  # Output: [1, 4, 9, 16, 25]

# Analysis of Time and Space Complexity:
# Time Complexity: The time complexity is O(n) because we iterate through the list of numbers from 1 to n exactly once.
# Space Complexity: The space complexity is O(n) because we are storing n squared numbers in the resulting list.


# Task 2
# Implement a function that has 3 parameters representing a list and 2 indices that will reverse a sublist within the list from index i to j (inclusive).

def reverse_sublist(arr, i, j):
    if i < 0 or j >= len(arr) or i > j:
        raise ValueError("Invalid indices")
    
    arr[i:j+1] = arr[i:j+1][::-1]
    
    return arr

print(reverse_sublist([10, 11, 12, 13, 14], 1, 3))  # Output: [10, 13, 12, 11, 14]

# Analysis of Time and Space Complexity:
# Time Complexity: The time complexity is O(j−i+1) because slicing and reversing a sublist of length j−i+1 takes linear time.
# Space Complexity: The space complexity is O(j−i+1) due to the temporary sublist created by slicing and reversing.


# Task 3
# Implement a function to merge two sorted lists into a single sorted list without using the built-in sorted function of list.sort method.

def concatenate_sorted_lists(lst1, lst2):
    concatenated_list = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            concatenated_list.append(lst1[i])
            i += 1
        else:
            concatenated_list.append(lst2[j])
            j += 1
    # print(concatenated_list) # Output: [20, 21, 22, 23, 24, 25]

    # Appending remaining elements:
    while i < len(lst1):
        concatenated_list.append(lst1[i])
        i += 1

    while j < len(lst2):
        concatenated_list.append(lst2[j])
        j += 1

    return concatenated_list

print(concatenate_sorted_lists([20, 22, 24, 26], [21, 23, 25]))  # Output: [10, 11, 12, 13, 14, 15, 16]


# Analysis of Time and Space Complexity:
# Time Complexity: The time complexity is O(n+m), where n is the length of lst1 and m is the length of lst2 because we traverse each list once.
# Space Complexity: The space complexity is O(n+m) because we are creating a new list of size n + m to store the concatenated elements.

line_break()

# ============ Dictionary Manipulation and Optimization ============

# Problem Statement: Explore advanced manipulation techniques and optimization strategies for Python dictionaries. Implement various dictionary operations and optimize them for improved performance.


# Task 1
# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

# # Expected Output
# {"a": 1, "b": 4, "c": 5, "d": 6}

def merge_two_dictionaries(dict_1, dict_2):
    merged_dict= dict_1.copy()
    merged_dict.update(dict_2)
    
    return merged_dict

print(merge_two_dictionaries(dict_1, dict_2)) # Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}


# Task 2
# Implement a function to find the difference of two dictionaries, i.e., keys that are only in one of the dictionaries along with their values.

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

# # Expected Output
# {"a": 1, "d": 6}

def difference_two_dictionaries(dict_1, dict_2):
    difference_dict = {}

    for key in dict_1:
        if key not in dict_2:
            difference_dict[key] = dict_1[key]
    
    for key in dict_2:
        if key not in dict_1:
            difference_dict[key] = dict_2[key]
    
    return difference_dict

print(difference_two_dictionaries(dict_1, dict_2))

# Task 3
# Implement a function to count the frequency of each unique word in a list using a dictionary. *Bonus* Ignore case 

def count_word_frequency(lst):
    word_occurrence = {}
    
    for word in lst:
        word = word.lower()  # Converting to lower case to ignore case (bonus)
        if word in word_occurrence:
            word_occurrence[word] += 1
        else:
            word_occurrence[word] = 1
    
    return word_occurrence

lst = ["mars", "Moon", "stars", "moon", "galaxy", "MARS", "MOON", "Stars"]

print(count_word_frequency(lst)) # Output: {'mars': 2, 'moon': 3, 'stars': 2, 'galaxy': 1}
