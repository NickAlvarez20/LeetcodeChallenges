# Define a function to calculate the transportation cost.
def calculate_transportation_cost(countries, transportation_costs):
    total_cost = 0
    for country in countries:
        total_cost += transportation_costs[country]
    return total_cost


# Presuming the countries you'll visit and the expected transportation costs for each
planned_countries = ["Germany", "Austria", "Switzerland"]
expected_costs = {"Germany": 200, "Austria": 180, "Switzerland": 220}

# TODO: Call the function and assign return value to transportation_cost
transportation_cost = calculate_transportation_cost(planned_countries, expected_costs)
print(f"The total transportation cost for the trip is: ${transportation_cost}")
