# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

highest = None

# create loop
while True:

# ask for user's input    
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break # break if the input is invalid
    
# display the highest number