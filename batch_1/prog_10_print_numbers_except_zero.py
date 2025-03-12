# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# set range up to 100 only
for num in range (101):
    if num % 10 != 0: # check if num is divisible by 10
        print (num) # print num
    