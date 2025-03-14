# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry

# Initialize variable to list

numbers = []
unique_numbers = []

# Input ten numbers

for i in range(10):
    num = float(input("Enter a number: "))
    if num not in unique_numbers:
        unique_numbers.append(num) # Adds only first entry
    numbers.append(num)

# Print ten number, for duplicates display the first entry of that number

print("Numbers entered (only first entry are kept): ", unique_numbers)