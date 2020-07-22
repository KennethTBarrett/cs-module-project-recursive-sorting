# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    i = j = 0  # We need two variables, one for the index of each array.

    array = []  # Array to populate and return.
    # This will continue until we've used all elements in one list.
    while i < len(arrA) and j < len(arrB):
        # Let's append the smaller value to the list.
        if arrA[i] < arrB[j]:  # If element in arrA is less than that in B...
            array.append(arrA[i])  # Append it.
            i += 1  # Add 1 to our index for arrA.
        else:  # Otherwise (if arrA element is greater than arrB element)
            array.append(arrB[j])  # Append it.
            j += 1  # Same thing, for arrB's index.
    # Extend whichever list was not completed to wrap it up!
    if i == len(arrA):  # If arrA was completed...
        array.extend(arrB[j:])  # Extend arrB, sliced at last index.
    else:  # If it wasn't (if arrB was completed)...
        array.extend(arrA[i:])  # Extend arrB, sliced at last index.
    return array


def merge_sort(arr):
    if len(arr) <= 1:  # This is our base case.
        return arr  # If the array is done with recursion, it'll return it.
    middle = len(arr) // 2  # Calculate the middle element.
    L = merge_sort(arr[:middle])
    R = merge_sort(arr[middle:])

    return merge(L, R)

# O(n log n) - Linearithmic run time
# This splits each array into two halves, then takes linear time to merge.

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
