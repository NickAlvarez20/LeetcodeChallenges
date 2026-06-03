class Solution:
    def isHappy(self, n: int) -> bool:
        # Create vars for data parsing
        squared_ints = []
        cycle_detection = set()
        # replace numbers by sum of square of its digit
        int_to_str = str(n)  # convert to string

        # iterate and sqaure each number, append to list
        for char in int_to_str:
            squared_ints.append(int(char) * int(char))
        sum_squared_outputs = sum(squared_ints)

        if sum_squared_outputs == 1:
            return True
        else:
            while sum_squared_outputs != 1:
                # convert to string
                sum_to_str = str(sum_squared_outputs)
                # reset squared_ints
                squared_ints = []
                for char in sum_to_str:
                    squared_ints.append(int(char) * int(char))
                sum_squared_outputs = sum(squared_ints)
                if sum_squared_outputs == 1:
                    return True
                # append sum squared outputs to set and check
                if sum_squared_outputs in cycle_detection:
                    break
                cycle_detection.add(sum_squared_outputs)

        return False
