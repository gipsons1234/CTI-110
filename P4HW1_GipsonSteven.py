 #Steven Gipson

 #4-12-2024

 #P4HW1

 #This program shows my understanding of lists and my ability to edit and enhance existing programs.


# Ask the user for the number of scores they want to enter
num_scores = int(input("How many scores would you like to enter? "))

# Initialize an empty list to store the scores
score_list = []

# Loop to collect the number of scores the user wants to enter
for i in range(num_scores):
    while True:
        # Ask the user to enter a score for each module
        score = float(input(f"Enter score {i + 1}: "))
        
        # Check if the score is valid (between 0 and 100)
        if 0 <= score <= 100:
            # If valid, add the score to the list and break out of the loop
            score_list.append(score)
            break
        else:
            # If invalid, notify the user and ask for a valid score
            print("Invalid score! Please enter a score between 0 and 100.")

print()  # Add a line break

# Display the lowest score entered
lowest_score = min(score_list)
print(f"Lowest score: {lowest_score:.2f}")

# Drop the lowest score from the list
modified_score_list = score_list.copy()
modified_score_list.remove(lowest_score)

# Display the score list after dropping the lowest score
print("Score list after dropping lowest score:", modified_score_list)

# Calculate the average of scores in the modified list
average_score = sum(modified_score_list) / len(modified_score_list)
print(f"Average Score: {average_score:.2f}")

# Determine the letter grade for the calculated average
if 90 <= average_score <= 100:
    letter_grade = 'A'
elif 80 <= average_score < 90:
    letter_grade = 'B'
elif 70 <= average_score < 80:
    letter_grade = 'C'
elif 60 <= average_score < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the letter grade to the user
print(f"Letter grade: {letter_grade}")
