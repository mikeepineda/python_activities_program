# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

for num in range(101):  # loop from 0 to 100
    if num % 10 != 0 and num % 10 != 5: # skip numbers ending in 0 or 5
        print(num)