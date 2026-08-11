# Provided function to choose states based on a budget constraint.
def choose_states(budget, costs):
    total_cost = 0
    chosen_states = []
    for state, cost in costs.items():
        if total_cost + cost > budget:
            break
        total_cost += cost
        chosen_states.append(state)
    return chosen_states


# TODO: Write a function named 'calculate_cost' that calculates the total cost of visiting the selected states.
# This function should take a list of states and a dictionary of state costs as arguments and return the total cost.
def calculate_cost(states, state_costs):
    total_cost = 0
    for state in states:
        total_cost += state_costs[state]
    return total_cost


# Sample data for budget and costs for demonstration
# You can test your function using this setup.
travel_budget = 3000
state_costs = {
    "California": 800,
    "Nevada": 600,
    "Arizona": 500,
    "Utah": 700,
    "Colorado": 900,
}

chosen_states = choose_states(travel_budget, state_costs)
trip_cost = calculate_cost(chosen_states, state_costs)

print(f"The states included in the road trip are: {chosen_states}")
print(f"The total cost of the road trip is: ${trip_cost}")
