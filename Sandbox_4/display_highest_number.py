# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# Initialize variable to list

numbers = []

# Input number until invalid

while True:
    try:
        num = float(input("Enter a number (or non-numeric to stop): "))
        numbers.append(num)  # Add number to the list
    except ValueError:
        print("Stopping input...")
        break  # Stop when the user enters an invalid input

# Print the highest number 

if numbers:
    print("The highest number:", max(numbers))
else:
    print("No valid numbers entered.")
