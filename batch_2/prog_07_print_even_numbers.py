#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

count = 0 # even number counter

# ask the user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0: # check if the number is even
        count += 1  


# print the count of even numbers
print("Even numbers count:", count)
