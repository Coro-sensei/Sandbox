# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Initialize the variable to list

numbers = []

# Input a number, continue until invalid

while True:
    try:
        num = float(input("Input a number (to stop, input non-numeric value): "))
        numbers.append(num)  # Add number to the list
    except ValueError:
        print("Stopping input...")
        break  # Stop when the user enters an invalid input

# Print lowest number
if numbers:
        print("The lowest number:", min(numbers))
else:
    print("No valid numbers, stopping the program.")