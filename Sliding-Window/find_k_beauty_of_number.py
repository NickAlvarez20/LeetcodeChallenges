class Solution(object):
    def divisorSubstrings(self, num, k):
        # setup tools
        str_num = str(num)
        L, result = 0, 0
        # expand
        for R in range(len(str_num)):
            if (R - L + 1) == k:
                curr_window = str_num[L : R + 1]
                conv_int_window = int(curr_window)
                if conv_int_window != 0 and num % conv_int_window == 0:
                    result += 1
                L += 1
        return result
