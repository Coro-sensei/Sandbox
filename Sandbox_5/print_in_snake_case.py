# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

# Input name 
name_of_user = input("Enter your name: ")

# Convert to snake casing 
snake_cased = name_of_user.lower().replace(" ", "_")

# Print the result
print("Name in snake_case: ", snake_cased)