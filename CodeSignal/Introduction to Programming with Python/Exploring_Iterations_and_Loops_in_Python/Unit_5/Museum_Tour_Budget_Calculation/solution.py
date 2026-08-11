# Planning a cultural tour and calculating the total and average admission cost for selected museums

planned_museums = [
    "Louvre",
    "British Museum",
    "Vatican Museums",
]  # Museums you plan to visit

# Admission costs in euros for each museum
museum_admission_costs = {
    "Louvre": 15,
    "British Museum": 0,
    "Vatican Museums": 20,
    "Prado Museum": 15,
}

total_admission_cost = 0
for museum in planned_museums:
    total_admission_cost += museum_admission_costs[museum]

# TODO: Compute the Average Admission Cost
average_admission_cost = total_admission_cost / len(planned_museums)

# TODO: Use the print statements correctly to display the total and average costs
print(f"The total admission cost for the museums is: €{total_admission_cost}")
print(f"The average admission cost per museum is: €{average_admission_cost:.2f}")
