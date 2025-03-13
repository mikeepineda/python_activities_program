# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = [] # store user input

# ask user to input 10 numbers
for i in range (10):
    num = int(input(f"Enter your number {i + 1}: "))
    numbers.append(num)

unique_numbers = []

# find numbers that don't have duplicate
for num in numbers: 
    if numbers.count(num) == 1:
        unique_numbers.append(num) 

# display result
print ("Numbers without duplicate:", unique_numbers)