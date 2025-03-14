# Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Initialize variable to list

numbers = []

# Input a number continue asking until invalid

while True:
    try:
        num = float(input("Input a number (to stop, input non-numeric input):"))
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num) # Adds unique to numbers
    except ValueError:
        print 
        break # Stops at invalid input

