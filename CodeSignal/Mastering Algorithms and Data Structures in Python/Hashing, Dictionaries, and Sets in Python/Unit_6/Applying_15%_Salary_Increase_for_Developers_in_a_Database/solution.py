import copy


def salary_increment(employees):
    bonus = 0
    for employee in employees:
        if employee["role"] == "developer":
            bonus = employee["salary"] * 0.15
            employee["salary"] += bonus
    return employees


# Test cases

employees = [
    {"name": "John", "role": "developer", "salary": 50000},
    {"name": "Mary", "role": "developer", "salary": 70000},
    {"name": "Jim", "role": "manager", "salary": 85000},
]

print(salary_increment(employees))
