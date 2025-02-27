"""
Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
"""

def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result
    
num = int(input("Enter a number : "))

factprial = get_factorial(num)

print(f"factorial of {num} is : {factprial}")