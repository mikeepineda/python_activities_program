# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

numbers = []

# ask user to input
# create loop
while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break # break if the input is invalid

# calculate
average = sum(numbers) / len(numbers)

# display the average
