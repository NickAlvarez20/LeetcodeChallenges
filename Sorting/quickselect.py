# To turn QuickSort into QuickSelect, we stop recursing on both sides. Instead, we only follow the path that contains our target index
# . This reduces the average time complexity from O(nlogn) to O(n)

# Python Implementation
# This function finds the
# -th smallest element (using 0-based indexing, so k = 0 is the minimum).

def quickselect(arr, k):
    # Basecase: if the list has only one element, return it
    if len(arr) == 1:
        return arr[0]

    # 1. Pick a pivot(middle element)
    pivot = arr[len(arr) // 2]

    # 2. Partition the array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 3. Determine which part holds the k-th element
    if k < len(left):
        # the target is in the left part
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        # the target is one of the lements equal to the pivot
        return middle[0]
    else: 
        # the target is in the right part
        # subtract the element we've already skipped (left + middle)
        new_k = k - len(left) - len(middle)
        return quickselect(right, new_k)

# Example usage:
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# Let's find the 3rd smallest element (index 2)
# Sorted would be [1, 1, 2, 3, 4, 5, 5, 6, 9] -> index 2 is '2'
result = quickselect(data, 2)
print(f"The 3rd smallest element is: {result}")
