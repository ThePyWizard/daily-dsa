#linear search in python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target1 = 4
result1 = linear_search(array, target1)
print(f"Index of {target1} in the array: {result1}")
