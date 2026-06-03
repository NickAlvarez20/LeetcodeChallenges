def two_sum_sorted(nums, target):
    # Declare left and right and set to start and end of array
    left, right = 0, len(nums)-1

    # while left is less than right (2 < 5)
    current_sum = nums[left] + nums[right] # checks value and adds to current sum
    if current_sum == target:
        return [left, right] #return left and right pointers and their index pos
    elif current_sum < target: #(2 < 7)
        left += 1 # Sum is too small, need a larger value (this is for sorted arrs)
    else:
        right -= 1 #Sum is too large (2,3,4,5) - decrement to find lower pair sum
    
    return [] #no pair found


