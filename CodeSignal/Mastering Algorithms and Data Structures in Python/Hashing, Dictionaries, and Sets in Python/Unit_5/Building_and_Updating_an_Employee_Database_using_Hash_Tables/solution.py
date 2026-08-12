# TODO: Create a Python dictionary to serve as a hash table
employee_database = {}

# TODO: Add employee names with their roles to the dictionary
employee_database["Tammy"] = "HR"
employee_database["Susan"] = "Sales"
employee_database["Jimothy"] = "Janitorial"

# TODO: Print the initial employee database
print(f"Initial Employee Database: {employee_database}")

# TODO: Update the role of an employee in the database
employee_database["Jimothy"] = "CEO"

# TODO: Print the database after the employee role update
print(f"Updated Employee Database: {employee_database}")

# TODO: Remove an employee from the database
del employee_database["Tammy"]

# TODO: Print the final employee database after the removal
print(f"Final State of Employee Database: {employee_database}")
