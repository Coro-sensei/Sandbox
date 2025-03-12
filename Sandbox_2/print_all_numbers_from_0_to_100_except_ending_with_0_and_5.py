# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# Initiate variable 

num = 0

# Print all numbers except numbers ending with zero and five

for num in range(101):

    if num % 10 != 0 and num % 10 != 5: # Checks for fives and zeroes
        
        print(num)