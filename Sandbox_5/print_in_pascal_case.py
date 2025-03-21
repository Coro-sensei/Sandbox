# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz 

# Input name in incorrect casing
name_of_user = input("Enter your name: ")

# Convert to pascal casing
pascal_cased = name_of_user.title().replace(" ", "")

# Print the result
print("Name in pascal case: ", pascal_cased)