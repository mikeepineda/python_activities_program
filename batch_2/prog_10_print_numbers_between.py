# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# ask user two inputs
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# determine the range
# find the smaller number and add 1, and find the larger number
for i in range (min(num1,num2) + 1,  max(num1,num2)):

# loop 
    print (i)