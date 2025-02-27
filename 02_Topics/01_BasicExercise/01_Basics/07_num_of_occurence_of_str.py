"""
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
"""

# Type 1 

# def number_of_occurence_of_str(list_string, mystring):
#     temp = 0
#     for item in range(len(list_string)):
#         if list_string[item] == mystring:
#             temp += 1
#     return temp

# mysentance = input("Enter a sentance : ")
# mystring = input("Enter a string : ")

# list_string = mysentance.split()

# print(f"{mystring} appeared {number_of_occurence_of_str(list_string, mystring)} times")

#--------------------------------------------------------------------------------------------------------------------
# Type 2 ; using inbuilt method


mysentance = input("Enter a sentance : ")
mystring = input("Enter a string : ")
occurence = mysentance.count(mystring)
print(f"{mystring} appeared {occurence} times")
