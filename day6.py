#Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the index number. If the highest element is not unique, print the index of the first instance.

def find_largest_element(lst):
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_value, max_index
numbers = [4, 8, 2, 10, 5, 8]
max_value, max_index = find_largest_element(numbers)
print(f"The largest element is {max_value} at index {max_index}.")
