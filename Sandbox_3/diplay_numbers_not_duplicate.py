# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.


# Initialize variable to zero

numbers = 0

# Input 10 numbers

for i in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Unique numbers checker 
unique = [num for num in numbers if numbers.count(num) == 1]

# Print all numbers that don't duplicate
print("These are the unique numbers: ", unique)
