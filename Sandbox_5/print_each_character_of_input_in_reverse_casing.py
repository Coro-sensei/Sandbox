# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz

# Input name with incorrect casing
name_of_user = input("Enter name: ")

# Convert to reverse incorrect casing 
inverse_casing = name_of_user.swapcase()

# Print the reverse incorrect casing
