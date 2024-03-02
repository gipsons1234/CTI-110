# Steven Gipson

# 3/2/2024

# P2Lab1

# This program calculates driving costs when given miles per gallon and the cost of gas.





# Input values
mileage = float(input("Enter the car's gas mileage (miles per gallon): "))
cost_per_gallon = float(input("Enter the cost of gas (dollars per gallon): "))

# Inserting a line break
print()

# Calculate the gas cost for different distances
distances = [20, 75, 500]
gas_costs = [distance / mileage * cost_per_gallon for distance in distances]

# Output the results rounded to the nearest hundredth
for distance, gas_cost in zip(distances, gas_costs):
    rounded_gas_cost = round(gas_cost, 2)
    print(f"For {distance} miles, the gas cost is ${rounded_gas_cost:.2f}")
