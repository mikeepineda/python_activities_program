# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = [] # store user input

# ask user to input 10 numbers
for i in range (10):
    num = int(input(f"Enter your number {i + 1}: "))
    numbers.append(num)