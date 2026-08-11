# Weekend getaway budget planning
weekend_budget = 1500
destination_costs = {"Beach": 600, "Mountain": 700, "Lake": 400}

total_spent = 0
chosen_destinations = []

# Let's select destinations for our weekend getaway without exceeding our budget
while total_spent < weekend_budget and destination_costs:
    destination, cost = destination_costs.popitem()
    if total_spent + cost <= weekend_budget:
        total_spent += cost
        chosen_destinations.append(destination)

print("Destinations chosen for the weekend getaway:", chosen_destinations)
