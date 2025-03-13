# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Initialize count to zero

odd_counter = 0

# Input ten numbers

for odd in range(10):
    num = float(input("Enter a Number: ")) 
    
    if num % 2 != 0: # Check the remainder if the number is odd
        odd_counter += 1

# Print the amount of odd numbers

print("Entered:"  , odd_counter)