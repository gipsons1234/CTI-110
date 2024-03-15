#Steven Gipson

#3-15-2024

#P3lab

#This program takes a year and determines if it is a leap year

#Ask the user to enter a year and stores the input as an integar
year = int(input('Enter a year: '))

#If the year is divisible by 4 and not by 100 OR if the year is divisible by 400 will print is a leap year. If anything else will print not a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
