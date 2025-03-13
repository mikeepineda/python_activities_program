# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# ask to input 10 numbers
for i in range (10):
    numbers = int(input(f"Enter your number {i + 1}: "))
# find duplicates
duplicates = set([num for num in numbers if numbers.count(num) > 1])
# display duplicates
if duplicates:
    print("Duplicate numbers:", *duplicates)
else:
    print("No duplicate numbers found.")