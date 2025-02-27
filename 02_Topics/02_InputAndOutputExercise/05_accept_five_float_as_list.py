"""
Exercise 5: Accept a list of 5 float numbers as an input from the user

Expected Output:
[78.6, 78.6, 85.3, 1.2, 3.5]
"""

num_list = []

for i in range(1, 6):
    float_num = float(input(f"Enter a float num{i} : "))

    num_list.append(float_num)

print(num_list)