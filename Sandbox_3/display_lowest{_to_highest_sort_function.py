# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# Initialize variable to list

numbers = []

# Input number, continue until invalid 

while True:
    try:
        num = float(input("Input a number (to stop, input non-numeric value): "))
        numbers.append(num)  # Add number to the list
    except ValueError:
        print("Stopping input...")
        break  # Stop when the user enters an invalid input

# Print lowest to highest with sort() function

if numbers:
    numbers.sort()
    print("Numbers from lowest to highest:", numbers)
else:
    print("No valid numbers, stopping the program.")
