# Binary searches uses divide and conquer approach to find a target value within a sorted list, isntead of checking everytime, you repeatedly split the search area in half

# iterative method is more memory efficient than recursion

# How It Works (Step-by-Step)
# Initialize Pointers: Set a low pointer at the start (index 0) and a high pointer at the end of the list.
# Find Midpoint: Calculate the middle index using floor division // to ensure you get an integer.
# Compare:
# If arr[mid] is your target, you're done! Return the index.
# If arr[mid] is smaller than the target, move your low pointer to mid + 1 to search the right half.
# If arr[mid] is larger than the target, move your high pointer to mid - 1 to search the left half.
# Repeat: Continue until the pointers cross (low > high), which means the element isn't there.
# W3Schools
# W3Schools
#  +9


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Check if the target is at the midpoint
        if arr[mid] == target:
            return mid

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1

        # if target is smaller, ignore the right half
        else:
            high = mid - 1

    # Return -1 (or None) if the target is not in the list

    return -1


# Example usage:
my_list = [10, 20, 30, 40, 50, 60]
print(binary_search(my_list, 40))  # Output: 3
