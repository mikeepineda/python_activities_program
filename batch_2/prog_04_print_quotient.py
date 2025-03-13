# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point.

# ask user two inputs
A = int(input ("Input your first number: "))
B = int(input ("Input your second number: "))

# print quotient of two inputs
print (A // B if B != 0 else "Undefined")