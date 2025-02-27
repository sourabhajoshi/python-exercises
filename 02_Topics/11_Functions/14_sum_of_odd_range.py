"""
Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
"""

def sum_of_odd(num):
    odd_sum = sum([i for i in range(num+1) if i%2 != 0])
    return odd_sum

num = int(input("Enter a number : "))
result = sum_of_odd(num)
print("Sum of even numbers : ", result)