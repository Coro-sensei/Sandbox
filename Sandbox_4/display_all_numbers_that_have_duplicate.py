# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Initialize variable to list

numbers = []
duplicates = set() # Set for duplicates

# Input ten numbers, check for duplicates

for i in range(10):
    num = float(input("Enter a number: "))
    if num in numbers:
        duplicates.add(num) # Add to duplicate numbers list
    numbers.append(num) # Store all numbers

# Print all numbers that have a duplicate

if duplicates:
    print("Numbers with duplicates: ", list(duplicates))
else:
    print("No duplicates found. ")
