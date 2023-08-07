def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    mid = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if list[mid] < item:
            low = mid + 1
        if list[mid] > item:
            high = mid - 1
        else: 
            return mid
            
        # If we reach here, then the element was not present
        return None
    

example_list = [9, 5, 1, 4, 3]

print(binarySearch(example_list, 40))



# Binary Search in python with Recursive
def binarySearchRecursive(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearchRecursive(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearchRecursive(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearchRecursive(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")