
def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min = j
        if min!=i:
            arr[i],arr[min]=arr[min],arr[i]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key = arr[i]
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

def partition(low,high,arr):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(low,high,arr):
    if low<high:
        pivot_index = partition(low,high,arr)
        quick_sort(low,pivot_index-1,arr)
        quick_sort(pivot_index+1,high,arr)
    return arr

def merge(left,right):
    i=j=0
    sorted = []
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    mid=len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def heapify(arr,heap_size,root):
    largest = root
    left = 2*root+1
    right = 2*root+2

    if left<heap_size and arr[left]>arr[largest]:
        largest = left

    if right<heap_size and arr[right]>arr[largest]:
        largest = right

    if largest !=root:
        arr[largest],arr[root]=arr[root],arr[largest]
        heapify(arr,heap_size,largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

array = [568,367,667,353,879,323,689,122]
# print(bubble_sort(array))
# print(selection_sort(array))
# print(insertion_sort(array))
# print(merge_sort(array))
# print(quick_sort(0,len(array)-1,array))
# print(heap_sort(array))
