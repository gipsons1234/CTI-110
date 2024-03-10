 #Steven Gipson

 #3-10-2024

 #P2HW2

 #This program shows my understanding of lists


# Ask the user to enter grades for each module
module_grades = []
module_grades.append(float(input("Module 1 grade: ")))
module_grades.append(float(input("Module 2 grade: ")))
module_grades.append(float(input("Module 3 grade: ")))
module_grades.append(float(input("Module 4 grade: ")))
module_grades.append(float(input("Module 5 grade: ")))
module_grades.append(float(input("Module 6 grade: ")))

print()  # Add a line break

print("------------Results------------")
# Display the lowest grade
lowest_grade = min(module_grades)
print(f"Lowest grade: {lowest_grade:.2f}")

# Display the highest grade
highest_grade = max(module_grades)
print(f"Highest grade: {highest_grade:.2f}")

# Calculate the sum of grades
sum_of_grades = sum(module_grades)
print(f"Sum of grades: {sum_of_grades:.2f}")

# Calculate the average grade
average_grade = sum_of_grades / len(module_grades)
print(f"Average grade: {average_grade:.2f}")
