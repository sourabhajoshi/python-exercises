"""
Find the largest item from a given list

x = [4, 6, 8, 24, 12, 2]
Expected Output:
24
"""

def get_largest_item(lst):
    largest_item = lst[0]
    for item in lst:
        if largest_item < item:
            largest_item = item
    return largest_item

lst = [4, 6, 8, 24, 12, 2]

largest_item = get_largest_item(lst)
print("From user defined function : ", largest_item)

print("From inbuilt function ", max(lst))



