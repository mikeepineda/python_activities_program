# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = [] # store user input
seen = set() # set to track seen numbers

# ask user to input 10 numbers
for i in range (10): 
    num = int(input(f"Enter your number {i + 1}: "))
    if num not in seen: # check if number is already displayed
        seen.add(num)   # mark as seen
    numbers.append(num) # store in list

print()     # display result

# create an empty set called displayed to track prints
displayed = set()  # Another set to track what we print
for num in numbers:
    if num not in displayed:
        print(num)
        displayed.add(num) # mark as printed
