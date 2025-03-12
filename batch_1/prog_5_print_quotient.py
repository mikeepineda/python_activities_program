# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point. 

# ask user two inputs
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# print quotient
print ("Quotient: ", num1/num2 if num2 != 0 else "Undefined")