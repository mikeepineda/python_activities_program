# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# add variable to store lowest number
lowest = None 

# ask for user's input
while True: 
    try: 
        num = int(input("Enter a number: "))

        # update lowest number
        if lowest is None or num < lowest:
            lowest = num
            
    except ValueError:
        break # break if the input is invalid
