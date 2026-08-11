# TODO: Define the budget for the cultural tour
budget = 2500
# TODO: Define the cost associated with each city visit
city_visit_cost = {"Melbourne": 500, "Rome": 800, "Paris": 900}

# TODO: Initialize the total amount spent and the list of chosen cities
total_spent = 0
list_of_chosen_cities = []

# TODO: Use a while loop to selectively add cities to the tour list based on the budget
while total_spent < budget and city_visit_cost:
    city, cost = city_visit_cost.popitem()
    if total_spent + cost < budget:
        total_spent += cost
        list_of_chosen_cities.append(city)
print(list_of_chosen_cities)

# Inside the loop:
# TODO: Retrieve a city and its associated cost
# TODO: Check if adding this city would exceed your budget
# TODO: If not, update the total spent and add the city to your list

# TODO: Print the list of cities chosen for the cultural tour
