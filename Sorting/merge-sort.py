# Merge-sort is a classic divide and conquer algorithm. It recursively splits an array in half until it reaches single element subarrays, then merges those subarrays backtogether in sorted order.

# How it works:
# Split: The array is repeatedly halved until you have several lists that each contain only one element.
# Compare: The algorithm takes two neighboring lists and compares their first elements.
# Merge: The smaller element is placed into a new combined list. This continues until all elements from both neighbors are merged into a single, sorted sub-list.
# Repeat: This "merging" bubbles back up the recursion tree until the entire array is reconstructed.


def merge_sort(arr):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the middle and split the list
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 2. Conquer: Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from both halves and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # add any remaining elements from either list
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


# Example usage:
data = [38, 27, 43, 3, 9, 82, 10]
print(f"Sorted array: {merge_sort(data)}")
