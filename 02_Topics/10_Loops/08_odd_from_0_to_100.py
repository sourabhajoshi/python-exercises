"""
Use for loop to iterate from 0 to 100 and print only odd numbers
"""

print("Method-1")
for i in range(101):
    if i%2 != 0:
        print(i, end=" ")
print()
print("Method-2")
for i in range(1, 100, 2):
    print(i, end=" ")