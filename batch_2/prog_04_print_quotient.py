# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point.

# ask user two inputs
num1 = int(input ("Input your first number: "))
num2 = int(input ("Input your second number: "))

# print quotient of two inputs
print (num1 // num2 if num2 != 0 else "Undefined")