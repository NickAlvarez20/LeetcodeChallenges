def repeating_elements(nums):
    seen, repeated = set(), set()

    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)

    return list(repeated)


print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))  # expected output : [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))  # expected output : []
