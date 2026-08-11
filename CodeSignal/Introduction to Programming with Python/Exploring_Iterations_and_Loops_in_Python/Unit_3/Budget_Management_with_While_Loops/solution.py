# We have a set budget for accommodations over the weekend
accommodation_budget = 300
hotel_costs = {"Hotel A": 90, "Hotel B": 120, "Hotel C": 85}

total_cost = 0
chosen_hotels = []

# TODO: Let's pick hotels for our weekend stay without exceeding our budget
while total_cost < accommodation_budget and hotel_costs:
    hotel, cost = hotel_costs.popitem()
    if total_cost + cost <= accommodation_budget:
        total_cost += cost
        chosen_hotels.append(hotel)  # Add the hotel to the list of chosen hotels

print("Hotels chosen for the weekend stay:", chosen_hotels)
