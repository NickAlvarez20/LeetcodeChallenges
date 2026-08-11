# TODO: Define a function called calculate_souvenir_budget
# TODO: The function should take two parameters: countries (a list of countries) and souvenir_costs (a dictionary with countries as keys and costs as values)
# TODO: Inside the function, create a variable to hold the total budget and set it to 0
# TODO: Use a for loop to iterate through the list of countries
# TODO: For each country, add the corresponding souvenir cost to the total budget
# TODO: The function should return the total budget
def calculate_souvenir_budget(countries, souvenir_costs):
    total_budget = 0
    for country in countries:
        total_budget += souvenir_costs[country]
    return total_budget


# Assuming the countries you'll visit and the average souvenir costs
countries = ["France", "Italy", "Spain"]
souvenir_costs = {"France": 150, "Italy": 100, "Spain": 75}

# Call the function
total_souvenir_budget = calculate_souvenir_budget(countries, souvenir_costs)
print(f"The total souvenir budget for the trip is: ${total_souvenir_budget}")
