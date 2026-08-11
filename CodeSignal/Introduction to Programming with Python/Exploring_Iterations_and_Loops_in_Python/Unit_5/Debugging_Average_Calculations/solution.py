# Attempting to calculate the total and average travel expenses, but something's not right.

chosen_countries = [
    "Germany",
    "Netherlands",
    "Belgium",
]  # Starting with these countries

# Each country's expected expenses
country_expenses = {
    "Germany": 850,
    "Netherlands": 760,
    "Belgium": 645,
    "Luxembourg": 730,
}

total_expense = 0
for country in chosen_countries:
    total_expense += country_expenses[country]

average_expense_per_country = total_expense / len(
    chosen_countries
)  # Seems we made a mistake here

print(f"The total expense for the trip is: €{total_expense}")
print(f"The average expense per country is: €{average_expense_per_country:.2f}")
