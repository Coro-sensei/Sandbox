# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
# Example: 
# Input: 143
# Output: 000143

# Input 0-1000 
numbers = str(input("Numbers inputted: "))

# Convert to a 6 digit format
if numbers.isdigit():
    print("Numbers in 6-digit format", numbers.zfill(6))

else:
    print("Numbers only!")



