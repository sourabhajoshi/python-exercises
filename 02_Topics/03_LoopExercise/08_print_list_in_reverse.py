"""
Exercise 8: Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]
Expected output:

50
40
30
20
10
"""

list1 = [10, 20, 30, 40, 50]

new_list = reversed(list1)

for item in new_list:
    print(item)
