"""
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
# new_list = []

# Method 1

# for i in range(len(list1)):
#     if list1[i]%2 != 0:
#         new_list.append(list1[i]) 

# for i in range(len(list2)):
#     if list2[i]%2 == 0:
#         new_list.append(list2[i]) 

# print("Result list : ", new_list)

# -------------------------------------------------------------------------------------------------------------------------------
# Method 2 : Using list comprehension to get odd numbers from list1 and even numbers from list2

new_list = [num for num in list1 if num%2 != 0] + [num for num in list2 if num%2 == 0]
print("Result list : ", new_list)

