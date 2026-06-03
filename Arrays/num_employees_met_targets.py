class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        good_employees = 0
        for employee in hours:
            if employee >= target:
                good_employees += 1
        return good_employees
