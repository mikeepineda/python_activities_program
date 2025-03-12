# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# ask user to input ten numbers
total = 0 

for i in range (10):
    num = float(input(f"Enter your number {i+1}: "))
    total += num

# print output
print("The sum of all numbers is : ", total)
