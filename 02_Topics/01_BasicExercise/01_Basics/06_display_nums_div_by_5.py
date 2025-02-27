"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
"""

def is_numbers_divisible_by_five(number):
    return number%5 == 0

size = int(input("Enter size of list : "))
numbers = []

for n in range(size):
    num = int(input(f"Enter a number for index {n} : "))
    numbers.append(num)

for num in range(len(numbers)):
    if is_numbers_divisible_by_five(numbers[num]):
        print(f"{numbers[num]}")



