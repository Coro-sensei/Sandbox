# Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Initiate counter

num_counter = 0

# Input ten numbers

for num in range(10):
    num = float(input("Enter a Number: "))
    num_counter.append(num)

# Compute the result 

num_minus_all = num_counter[0] - sum(num_counter[1:])

# Print result of first number minus all of the remaining numbers
print("Result of the first number minus all of the remaining number: ", num_minus_all)