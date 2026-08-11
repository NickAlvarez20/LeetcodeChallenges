# TODO: Define a list named chosen_countries with countries selected for the road trip
chosen_countries = ["Spain", "Portugal", "France", "Sweden"]

# TODO: Define a dictionary named country_fuel_costs with fuel costs for countries
country_fuel_costs = {"Spain": 150, "Portugal": 95, "France": 50, "Sweden": 450}

# TODO: Initialize a variable total_fuel_cost to 0
total_fuel_cost = 0

# TODO: Use a for loop to add up the fuel cost for each chosen country
for country, fuel in country_fuel_costs.items():
    total_fuel_cost += fuel

# TODO: Calculate the average fuel cost per country

average_fuel_cost = total_fuel_cost / len(chosen_countries)

# TODO: Print the total fuel cost for the road trip

print(f"The total fuel costs for the road trip is ${total_fuel_cost}")

# TODO: Print the average fuel cost per country
print(f"The average fuel cost per country is ${average_fuel_cost:.2f}")
