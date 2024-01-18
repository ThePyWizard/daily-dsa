#binary search on a sorted array

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 

    return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 5
result1 = binary_search(sorted_array, target1)
print(f"Index of {target1} in the array: {result1}")

