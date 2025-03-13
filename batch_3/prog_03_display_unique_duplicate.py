# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# create a list to store user's input
numbers = []

# ask for user's input
while True:
    try:
        num = int(input("Enter a number:"))
    # check if num is a duplicate
        if num in numbers:
            print ("Duplicate") 
        else:
            print ("Unique")
            numbers.append(num) # store only unique numbers

# exit loop if the input is invalid
    except ValueError: 
        print ("Input invalid. The program will stop.")
        break