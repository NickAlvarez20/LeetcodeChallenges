# Define a function to calculate the total enjoyment score.
def calculate_total_enjoyment(cities, city_enjoyment_scores):
    total_enjoyment = 0
    for city in cities:
        total_enjoyment += city_enjoyment_scores[city]
    return total_enjoyment


# Presuming the chosen_cities and their enjoyment scores
chosen_cities = ["Rome", "Paris", "Barcelona"]
city_enjoyment_scores = {"Rome": 8, "Paris": 9, "Barcelona": 10}

# Call the function
total_enjoyment = calculate_total_enjoyment(chosen_cities, city_enjoyment_scores)
print(f"The total enjoyment score of the trip is: {total_enjoyment}")
