# Define a function to calculate the total dining cost.
def calculate_dining_cost(countries, dining_costs):
    total_cost = 0
    for country in countries:
        total_cost += dining_costs[country]
    return total_cost


# Assuming the countries you'll visit and the expected dining costs for each
visited_countries = ["Germany", "Netherlands", "Belgium"]
expected_costs = {"Germany": 300, "Netherlands": 250, "Belgium": 200}

# Call the function
dining_cost = calculate_dining_cost(visited_countries, expected_costs)
print(f"The total dining cost for the trip is: ${dining_cost}")
