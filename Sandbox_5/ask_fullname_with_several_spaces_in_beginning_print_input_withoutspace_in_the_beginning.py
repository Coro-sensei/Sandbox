# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
# Example: 
# Input:          Juan Dela Cruz
# Output: Juan Dela Cruz

# Input the name 
name_of_user = input("Enter name: ")

# Remove the several spaces 
removed_spaces = name_of_user.lstrip()

# Print the result
print("Name: ", removed_spaces)