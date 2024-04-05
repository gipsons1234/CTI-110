#Steven Gipson

#4-5-2024

#P4Lab2

#This program tests my knowledge of how to write code that displays information to users


# Prompt the user to input the first integer
num1 = int(input("Enter the first integer: "))

# Prompt the user to input the second integer
num2 = int(input("Enter the second integer: "))

# Check if the second integer is less than the first
if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    # Output the first integer
    print(num1, end=' ')

    # Output subsequent increments of 5 until it's less than or equal to the second integer
    while num1 + 5 <= num2:
        num1 += 5
        print(num1, end=' ')

    # End with a newline
    print()
