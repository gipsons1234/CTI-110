#Steven Gipson

#4-28-24

#P5HW

#Math Quiz (using loops, functions and module to create a math quiz)


import random
#Generate random numbers
def generate_random_numbers():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    return num1, num2
#Display random numbers
def display_numbers(num1, num2, operation):
    print(num1)
    if operation == 'add':
        print("+" + str(num2))
    elif operation == 'subtract':
        print("-" + str(num2))

def get_user_answer():
    return int(input("Enter the result of the operation: "))
#Display main menu
def main():
    print("Welcome to Math Quiz")
    while True:
        print("\nMain Menu:")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            operation = 'add'
        elif choice == '2':
            operation = 'subtract'
        elif choice == '3':
            print("Exiting the program.")
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")
            continue

        num1, num2 = generate_random_numbers()
        display_numbers(num1, num2, operation)
#Adds numbers       
        if operation == 'add':
            actual_answer = num1 + num2
#Subtracts numbers            
        elif operation == 'subtract':
            actual_answer = num1 - num2

        num_guesses = 0
#Gets number of guesses
        while True:
            user_answer = get_user_answer()
            num_guesses += 1
#If answer is correct
            if user_answer == actual_answer:
                print("Correct!")
                print("Number of guesses:", num_guesses)
                break
#If answer is incorrect            
            elif user_answer > actual_answer:
                print("Too high. Please try again.")
            else:
                print("Too low. Please try again.")

if __name__ == "__main__":
    main()
