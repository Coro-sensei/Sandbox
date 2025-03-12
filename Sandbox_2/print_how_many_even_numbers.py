# Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Initialize to zero
even_counter = 0

# Input ten numbers

for i in range(10):

    num = float(input("Enter ten numbers: "))
    if num % 2 == 0: # Check for even numbers 
        even_counter += 1 # Keep track of count

# Print how many even numbers
print(even_counter)
