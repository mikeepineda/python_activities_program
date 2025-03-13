# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

numbers = []  

# ask 10 numbers from user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# compute the result
result = numbers[0] - sum(numbers[1:])

# print the result
print("Result:", result)

