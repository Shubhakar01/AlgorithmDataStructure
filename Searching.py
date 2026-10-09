def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

unsorted_nums = [64, 34, 25, 12, 22, 11, 90]
target_val = 22

lin_idx = linear_search(unsorted_nums, target_val)
print(f"Linear Search on {unsorted_nums}:")
print(f"Target {target_val} found at index: {lin_idx}\n")

sorted_nums = [11, 12, 22, 25, 34, 64, 90]

bin_idx = binary_search(sorted_nums, target_val)
print(f"Binary Search on {sorted_nums}:")
print(f"Target {target_val} found at index: {bin_idx}")