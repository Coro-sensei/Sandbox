# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry

# Initialize variable to list

numbers = []

# Input ten numbers

for i in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Print ten number, for duplicates display the first entry of that number
