# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# import counter
from collections import Counter

# add empty list for user's input
numbers = []

# ask user's input
while True: 
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break # break when the input is invalid

# find the most frequent nummber
if numbers:
    freq_count = Counter(numbers)
    most_freq = max(freq_count, key=freq_count.get)

# print display
    print(f"The number with the most duplicates is: {most_freq} (appeared {freq_count[most_freq]} times)")
else:
    print("No numbers were entered.")
