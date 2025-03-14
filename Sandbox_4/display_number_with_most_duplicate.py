# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

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

# Print number with the most duplicate

if numbers:
    frequency = {}  # Dictionary to count occurrences
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    most_common = max(frequency, key=frequency.get)  # Get the most frequent number
    print("Number with the most duplicates:", most_common)
else:
    print("No valid numbers entered.")