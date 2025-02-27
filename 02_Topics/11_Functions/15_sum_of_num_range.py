"""
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
"""

def sum_of_numbers(num):
    sum_of_nums = sum([i for i in range(num+1)])
    return sum_of_nums

num = int(input("Enter a number : "))
result = sum_of_numbers(num)
print("Sum of even numbers : ", result)