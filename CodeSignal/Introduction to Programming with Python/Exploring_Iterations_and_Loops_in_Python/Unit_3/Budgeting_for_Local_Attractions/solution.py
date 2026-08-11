# We have a budget for a local tour and each attraction costs a certain amount
local_tour_budget = 150
attraction_costs = {"Museum": 50, "Art Gallery": 40, "Historical Site": 30}

total_spent = 0
selected_attractions = []

# Let's select attractions for our local tour without exceeding our budget
while total_spent < local_tour_budget and attraction_costs:
    attraction, cost = attraction_costs.popitem()
    if total_spent + cost <= local_tour_budget:
        total_spent += cost
        selected_attractions.append(attraction)

print("Attractions selected for the local tour:", selected_attractions)
