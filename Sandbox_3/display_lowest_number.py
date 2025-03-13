# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Initialize th variable to zero

numbers = 0

# Input a number, continue until invalid

while True:
    num = float(input("Input a number (to stop input non-numeric input): "))
    numbers.append(num) # Adds number to the variable numbers

# Print lowest number