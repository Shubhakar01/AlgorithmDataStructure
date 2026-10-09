"""
Simple Sorting Algorithms Collection in Python
"""


def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def heap_sort(arr):
    def heapify(items, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and items[left] > items[largest]:
            largest = left
        if right < n and items[right] > items[largest]:
            largest = right

        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            heapify(items, n, largest)

    data = arr.copy()
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

    return data


nums = [64, 34, 25, 12, 22, 11, 90, -5, 0, 42]

print("Original: ", nums)
# print("Bubble:   ", bubble_sort(nums))
# print("Selection:", selection_sort(nums))
# print("Insertion:", insertion_sort(nums))
# print("Quick:    ", quick_sort(nums))
# print("Merge:    ", merge_sort(nums))
print("Heap:     ", heap_sort(nums))