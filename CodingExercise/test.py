# 1. Reverse a List

array_list = []

for i in range(0, 101):
    array_list.append(i)

# reversed_list = array_list[::-1]
# print(reversed_list)

# --------------------------------------------------------------------------

# 2. Find the Maximum
# do not use built in max

# Ok, sort reverse order and retrieve first index
# sorted_arr = sorted(array_list, reverse=True)
# max_val = sorted_arr[0]
# print(f"The max value is {max_val}")

# --------------------------------------------------------------------------

# 3. Rotate elements
# Shift all elements to the right by k steps
# ok use list slicing
# k = 2

# # shift right by k steps
# shift_right = array_list[-k:] + array_list[:-k]
# print(f"The array after right shift: {shift_right}")

# # shift left by k steps
# shift_left = array_list[k:] + array_list[:k] # so grab a slice from k to end, and then that will be the starting position then add the other slice from the start until k
# print(f"The array after left shift: {shift_left}")

# # Practice using double ended queue
# from collections import deque
# d = deque(array_list)
# d2 = deque(array_list)
# d.rotate(2) # Shift right
# d2.rotate(-2) # Shift left

# compare_shifts_right = True if shift_right == list(d) else False
# compare_shifts_left = True if shift_left == list(d2) else False

# print(f"Does shift right match deque shift right? {compare_shifts_right}")
# print(f"Does shift left match deque shift left? {compare_shifts_left}")

# --------------------------------------------------------------------------

# 4. Remove duplicates
# take a list and return a new list with unique elements, while preserving original order
# duplicates_arr = [1, 2, 2, 3, 4, 4, 5]
# removed_duplicates = set(duplicates_arr)
# print(list(removed_duplicates))

# --------------------------------------------------------------------------

# 5. Count occurences
# Count how many times each item appears in a list.Return the counts as a dictionary.

# input_arr = ['a', 'b', 'a', 'c', 'b', 'a']
# # create a dict
# counts_dict = {}
# for ele in input_arr:
#     if ele in counts_dict:
#         counts_dict[ele] += 1
#     else:
#         counts_dict[ele] = 1
# print(counts_dict)

# # Use get method
# counts_dict = {} # reset
# for ele in input_arr:
#     counts_dict[ele] = counts_dict.get(ele, 0) + 1
# print(f"Using .get method: {counts_dict}")

# # Using collections . Counter
# from collections import Counter
# counts_dict = Counter(input_arr)  # reset
# print(f"Using Counter tool: {counts_dict}")

# --------------------------------------------------------------------------

# 6. Move Zeros
# Move all zeros to end of the list and maintain relative order
# arr_input = [0, 1, 0, 3, 12]

# # Method 1: Use two pointers to modify array in place
# def moves_zeroes(arr):
#     j = 0 # Pointer for the next non-zero element position

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             # Python in place swap
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
#     return arr

# print(moves_zeroes(arr_input))

# # Method 2: List comprehension


# def move_zeroes_simple(arr):
#     # Filter all non-zero elements
#     non_zeroes = [x for x in arr if x != 0]

#     # Calculate how many zeroes are missing
#     zeroes = [0] * (len(arr) - len(non_zeroes))

#     # Combine the two lists
#     return non_zeroes + zeroes

# print(move_zeroes_simple(arr_input))

# # Method 3: Use lambda with custom key

# lambda_zero_arr = arr_input
# lambda_zero_arr.sort(key=lambda x: x==0)


# print(f"Using lambda sort {lambda_zero_arr}")


# --------------------------------------------------------------------------

# 7. Find Common Items

# input_one_arr = [1,2,3,4]
# input_two_arr = [3,4,5,6]
# output = []

# for item in input_one_arr:
#     if item in input_two_arr:
#         output.append(item)
# print(f"Common items found between 1 and 2: {output}")

# # Use sets with intersection
# # Use and operator

# output1 = list(set(input_one_arr)&set(input_two_arr))
# print(f"Common items found between 1 and 2: {output1}")

# # Set Lookup (Preserves Original Order)
# # Convert to set for O(1) instant lookup
# set_two = set(input_two_arr)

# # Filter items using a list comprehension
# output2 = [item for item in input_one_arr if item in set_two]
# print(f"Common items found between 1 and 2: {output2}")


# --------------------------------------------------------------------------

# 8. Cumulative Sum
# Create a new list where each element is sum of itself and all previous elements
# input_arr = [1, 2, 3, 4]
# # Expected output : [1, 3, 6, 10]
# result = []
# curr_sum = 0

# for num in input_arr:
#     curr_sum += num
#     result.append(curr_sum)
# print(result)


# --------------------------------------------------------------------------

# 9. Merge Sorted LIsts

# Combine two pre-sorted lists into one single sorted list
# Do not use built in sort() or sorted() functions
# input_1 = [1, 3, 5]
# input_2 = [2, 4, 6]
# Expected output Output: ([1,2,3,4,5,6]

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]

#         merge_sort(L)
#         merge_sort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]: # Ascending
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

# combine_arr = input_1 + input_2
# merge_sort(combine_arr)


# print(combine_arr)

# List is pre-sorted so only use the merge portion


# def merge(L, R):
#     arr = [0] * (len(L) + len(R))
#     i = j = k = 0

#     while i < len(L) and j < len(R):
#         if L[i] < R[j]:  # Ascending
#             arr[k] = L[i]  # updates k pos
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     while i < len(L):
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < len(R):
#         arr[k] = R[j]
#         j += 1
#         k += 1

#     return arr


# print(merge(input_1, input_2))

# --------------------------------------------------------------------------

# 10. Split in halves
# Split a single list into two equal halves.
# If the length is odd, put the extra element in the first half.

# input_arr = [1, 2, 3, 4, 5, 6]


# def split_halves(arr):
#     mid_point = len(arr) // 2
#     if len(input_arr) % 2 == 1:
#         first_halve = input_arr[: mid_point + 1]
#         second_halve = input_arr[mid_point + 1 :]
#     else:
#         first_halve = input_arr[:mid_point]
#         second_halve = input_arr[mid_point:]
#     return [first_halve, second_halve]


# print(split_halves(input_arr))


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


# Strings


# 1. The Pointer Swap (String Reversal)

# string_example = 'The great warm up practice results in daily discipline'

# # Two pointers and reverse using Python swap
# left = 0
# right = len(string_example) - 1
# conv_list = list(string_example)

# while left < right:
#     conv_list[left], conv_list[right] = conv_list[right], conv_list[left]
#     left += 1
#     right -= 1

# reversed_string = "".join(conv_list)
# print(reversed_string)

# --------------------------------------------------------------------------

# 2. The Case Inverter
# Goal: Convert lowercase letters to uppercase and vice versa without using built-in .toUpperCase() or .toLowerCase().

# test_str = 'GeEkSfOrGeEkS'

# # strings are immutable so need list
# conv_str = list(test_str)
# result = []

# for char in conv_str:
#     if char.isupper():
#         temp = ord(char)
#         new_char = temp + 32
#         result.append(chr(new_char))
#     elif char.islower():
#         temp_2 = ord(char)
#         new_char_2 = temp_2 - 32
#         result.append(chr(new_char_2))
#     else:
#         result.append(char)

# final_res = "".join(result)
# print(final_res)


# while index < len(chars_list):
#     if chars_list[index].isupper():
#         temp = ord(chars_list[index])
#         conv_char = temp + 32
#         lower_char = chr(conv_char)
#         res.append(lower_char)
#     elif chars_list[index].islower():
#         temp = ord(chars_list[index])
#         conv_char = temp - 32
#         upper_char = chr(conv_char)
#         res.append(upper_char)
#     else:
#         res.append(chars_list[index])
#     index += 1


# joined_chars = "".join(res)
# print(joined_chars)

test_str = "GeEkSfOrGeEkS"

# immutable strings
result = []

for char in test_str:
    if "A" <= char <= "Z":
        temp = ord(char) + 32
        result.append(chr(temp))
    elif "a" <= char <= "z":
        temp = ord(char) - 32
        result.append(chr(temp))
    else:
        result.append(char)

joined_chars = "".join(result)

print(joined_chars)


# --------------------------------------------------------------------------


# Palindrome

# Two pointers

test_str_1 = "Palindrome"
test_str_2 = "racecar"


def check_palindrome(str):
    # Two pointer approach
    left = 0
    right = len(str) - 1
    is_palindrome = True

    while left < right:
        if str[left] != str[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    return is_palindrome


def check_palindrome_for(str):
    length = len(str)

    for i in range(length // 2):
        if str[i] != str[length - 1 - i]:
            return False
    return True


def check_palindrome_for_var_2(str):
    left = 0
    right = len(str) - 1

    for _ in str:
        if left >= right:
            break

        if str[left] != str[right]:
            return False

        left += 1
        right -= 1
    return True


print(check_palindrome(test_str_1))
print(check_palindrome(test_str_2))

print(check_palindrome_for(test_str_1))
print(check_palindrome_for(test_str_2))

print(check_palindrome_for_var_2(test_str_1))
print(check_palindrome_for_var_2(test_str_2))


