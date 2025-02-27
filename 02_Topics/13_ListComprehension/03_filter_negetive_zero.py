"""
Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print("Original list : ", numbers)

new_list = [i for i in numbers if i<=0]

print("New list : ", new_list)