# Steven Gipson

# 3/2/2024

# P2Lab2

# This program takes integers and finds the product and average as integers and then as integers to 3 decimal places.


# Input the four floating-point numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Add a line break
print()

# Calculate product and average
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Output as integers (rounded)
print(f"Product: {int(product)}")
print(f"Average: {int(average)}")

# Add a line break
print()

# Output as floating-point numbers
print(f"Product out to three digits after the decimal: {product:.3f}")
print(f"Average out to three digits after the decimal: {average:.3f}")
