# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

numbers = []

# create loop
while True:

# ask user to input number
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break  # break loop if the input's invalid

# sort and display numbers from highest to lowest
