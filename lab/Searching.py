def linear_search(arr,key):
    for element in arr:
        if element == key:
            return True
    return False

def binary_search(arr,low,high,key):
    if low>high:
        return False
    mid = (low+high)//2
    if(arr[mid]==key):
        return True
    if key<arr[mid]:
        return binary_search(arr,low,mid-1,key)
    else:
        return binary_search(arr,mid+1,high,key)

def main():
    arr = [12,23,34,45,56,67,78,89,90]
    if linear_search(arr,45):
        print("Element is Present")
    else:
        print("Element not present")

    if binary_search(arr,0,len(arr)-1,45):
        print("Element is Present")
    else:
        print("Element not present")

main()