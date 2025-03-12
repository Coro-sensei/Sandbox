# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Initialize count

sum_counter = 0

# Input ten numbers 

for i in range (10):
    sum_counter += float(input("Enter the ten numbers: "))


#  Print the sum of the ten numbers
print (sum_counter)