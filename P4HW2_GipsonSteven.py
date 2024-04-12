#Steven Gipson

#4-12-2024

#P4HW2

#This assignment assess my understanding of decision structures and my ability to edit and enhance existing programs.


# Variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

# Gather employee information
while True:
    # Ask the user to enter employee's name
    employee_name = input("Enter employee's name (or 'Done' to finish): ")
    
    # Check if the user wants to terminate the program
    if employee_name.lower() == 'done':
        break
    
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

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    num_employees += 1

    # Print the headers after entering the pay rate for each employee
    print("\nPay Rate   Hours Worked   Overtime   OvertimePay   RegHour Pay   Gross Pay")
    print("---------------------------------------------------------------------------")

    # Print the values using for each employee
    format_string = "{:<10.2f} {:<14.2f} {:<9.2f} {:<13.2f} {:<12.2f} {:<10.2f}"
    print(format_string.format(pay_rate, hours_worked, overtime_hours, overtime_pay, regular_pay, gross_pay))

# Print summary of employee pays after entering "Done"
if num_employees > 0:
    print("\nSummary of Employee Pays")
    print("------------------------")
    print("Number of Employees Entered:", num_employees)
    print("Total Overtime Pay:", total_overtime_pay)
    print("Total Regular Pay:", total_regular_pay)
    print("Total Gross Pay:", total_gross_pay)
   

