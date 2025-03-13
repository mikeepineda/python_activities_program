# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# import counter
from collections import Counter

# add empty list for user's input
numbers = []

# ask user's input
num = int(input("Enter a number (or any non-number to stop): "))
numbers.append(num)

# break when the input is invalid
# find the most frequent nummber
# print display
