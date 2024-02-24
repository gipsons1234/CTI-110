# Steven Gipson
# 2-24-2024
# P1HW2
# This assignment does basic math on entered numbers

# Ask user for their budget
budget = float(input("Enter your budget: \n "))

# Ask user for travel destination
destination = input("Enter your travel destination: \n ")

# Ask user for amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas? \n"))

# Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need to accomdation/hotel? \n"))

# Ask user for amount they will spend on food
food_expense = float(input("Last, how much do you need for food? \n"))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract total expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("------------Travel Expenses------------ \n")
print(f"Location: {destination}")
print (f"Initial Budget: ${budget}\n")
print(f"Fuel: ${gas_expense} on gas")
print(f"Accomodation: ${accommodation_expense}")
print(f"Food: ${food_expense} on food\n")
print(f"You will spend ${total_expenses} on gas, accommodation, and food\n")
print(f"Remaining Balance ${remaining_budget}\n")
