# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# add list to store user input
numbers = []

# ask for user's input
while True: 
    try: 
        num = int(input("Enter a number: "))
        numbers.append(num) # store valid number
    except ValueError:
        break # break if the input is invalid

# display num from lowest to highest
if numbers: 
    print ("Numbers in ascending order:", numbers)
else: 
    print ("No valid numbers were entered.")
