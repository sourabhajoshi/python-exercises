"""
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:
Given list: [10, 20, 30, 40, 10]
result is True
numbers_y = [75, 65, 35, 75, 30]
result is False
"""

def check_first_last_same(numbers):
    """Check if the first and last numbers in the list are the same."""
    if not numbers:
        return False
    else:
        return numbers[0] == numbers[-1]

size = int(input("Enter size of list : "))
numbers = []

for number in range(size):
    num = int(input(f"Enter number for index {number}: "))
    numbers.append(num)

result = check_first_last_same(numbers)

print(f"Given list: {numbers}")
print(f"Result is {result}")