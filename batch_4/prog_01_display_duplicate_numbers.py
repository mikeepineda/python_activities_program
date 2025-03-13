# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = [] # store user input

# ask user to input 10 numbers
for i in range (10):
    num = int(input(f"Enter your number {i + 1}: "))
    numbers.append(num)

# find numbers that have duplicate
for num in numbers: 
     if numbers.count(num) > 1 and num not in duplicate_numbers:
        duplicate_numbers.append(num) 