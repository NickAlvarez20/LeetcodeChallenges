var plusOne = function (digits) {
  let n = digits.length;
  for (let i = n - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits;
    }
    digits[i] = 0;
  }
  return [1, ...digits];
};

// Intuition: Edge cases for any digit not 9, simple, increment once and exit
// If last number in array is nine, we can carry the one and change current pos to 0
// use spread operator for last edge case, if all numbers are 9 then use carry-over from basic addition
// math to correctly update. Draw this out on paper to see 999+1= 1000.

//Time complexity: O(n) - Worst case we traverse the entire array at once(all 9s), best case O(1) if last digit < 9
//Space complexity: O(1) - Modify the input array in-place, no extra memory needed
// The only extra space is the new array in the all 9s case, but that's O(n) space for output, which is allowed and (unavoidable). Most interviewers consider this O(1) auxiliary space.
