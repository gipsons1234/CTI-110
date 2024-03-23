#Steven Gipson

#3-23-2024

#P3HW2

#This assignment assess my understanding of decision structures.



# Ask the user to enter employee's name
employee_name = input("Enter employee's name: ")

# Ask user to enter number of hours worked and pay rate
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Check if employee has worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
else:
    overtime_hours = 0

# Calculate overtime pay and pay for regular hours
if overtime_hours > 0:
    overtime_pay = 1.5 * pay_rate * overtime_hours
    regular_pay = 40 * pay_rate
else:
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("\nEmployee Name:", employee_name)
print("-----------------------")

# Print the headers
print("Pay Rate   Hours Worked   Overtime   OvertimePay   RegHour Pay   Gross Pay")
print("---------------------------------------------------------------------------")

# Define the widths
format_string = "{:<10.2f} {:<14.2f} {:<9.2f} {:<13.2f} {:<12.2f} {:<10.2f}"

# Print the values using the defined format
print(format_string.format(pay_rate, hours_worked, overtime_hours, overtime_pay, regular_pay, gross_pay))

