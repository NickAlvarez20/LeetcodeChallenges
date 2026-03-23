# QuickSort is often the go-to sorting algorithm because it’s usually faster in practice than Merge Sort, even though they share similar logic. It’s a divide and conquer algorithm that picks a "pivot" and partitions the array around it.

# Pivot Selection: You pick one number from the array. Everything will be compared against this "pivot."
# Partitioning: You move everything smaller than the pivot to the left and everything larger to the right.
# Recursion: You repeat the process for the left side and the right side until you’re left with single-element lists.
# Combine: As the recursion "unwinds," the sorted pieces are glued back together.

def quicksort(arr):
    # Base case: 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # 1. Pick a pivot
    # (middle element is usually safer than the first)
    pivot = arr[len(arr) // 2]

    # 2. Partition the array into three parts
    left = [x for x in arr if x < pivot] # elements smaller than the pivot
    middle = [x for x in arr if x == pivot] # element equal to pivot
    right = [x for x in arr if x > pivot] # elements larger than pivot

    # 3. Recursively sort the left and right, then combine
    return quicksort(left) + middle + quicksort(right)

# Example usage:
data = [33, 10, 55, 71, 29, 10, 5, 42]
print(f"Sorted array: {quicksort(data)}")
