"""
Iterate 10 to 0 using for loop, do the same using while loop.
"""

print("Iterate 10 to 0 using for loop")
for i in range(10, -1, -1):
    print(i)

print("-"*50)
print("Iterate 10 to 0 using while loop")
id = 10
while id >= 0:
    print(id)
    id = id - 1