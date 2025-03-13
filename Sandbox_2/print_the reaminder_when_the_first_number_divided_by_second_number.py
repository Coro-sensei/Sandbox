# Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# Input two numbers

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

# Print remainder of the first number and second number

if num2 != 0: # Check if the num2 is zero because we can't divide by zero
    remainder = num1 % num2
    print("Remainder: ", remainder)
