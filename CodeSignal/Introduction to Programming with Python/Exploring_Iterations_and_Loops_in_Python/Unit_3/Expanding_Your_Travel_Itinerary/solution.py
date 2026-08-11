# We have a budget for the trip and each country costs a certain amount
travel_budget = 5000
# TODO: Add "Greece" to the country_costs dictionary with a cost and observe how it changes the final output.
country_costs = {
    "France": 1000,
    "Italy": 800,
    "Spain": 900,
    "Japan": 1200,
    "Greece": 950,
}

total_cost = 0
chosen_countries = []

# Let's add countries to our trip until our budget runs out using a while loop
while total_cost < travel_budget and country_costs:
    country, cost = country_costs.popitem()
    if total_cost + cost <= travel_budget:
        total_cost += cost
        chosen_countries.append(country)

print("Countries chosen for the trip:", chosen_countries)
