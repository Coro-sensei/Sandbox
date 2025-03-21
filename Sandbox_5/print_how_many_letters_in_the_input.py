# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# Input a complete statement
statement_of_user = input("Enter your statement: ")

# Count the numbers in the input
count_words_statement = len(statement_of_user.split()) 

# Print the result 
print("How many words in your statement: ", count_words_statement)