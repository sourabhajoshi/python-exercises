"""
Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
"""

def sum_of_even(num):
    sum_res = sum([i for i in range(num+1) if i%2==0])
    return sum_res

num = int(input("Enter a number : "))
result = sum_of_even(num)
print("Sum of even numbers : ", result)