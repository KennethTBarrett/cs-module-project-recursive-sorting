# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Let's first ensure the start is greater than the end.
    if start > end:
        return -1  # If it's not, we're supposed to return -1 (not found)
    middle = (start + end) // 2  # Calculate the middle.
    # If we are at the target, go ahead and return the 'middle'
    if target == arr[middle]:
        return middle
    # If the target is less than the middle array index, take 1 off the middle.
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle-1)
    # If the target is greater than the middle array index, add 1 to the middle.
    elif target > arr[middle]:
        return binary_search(arr, target, middle+1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
