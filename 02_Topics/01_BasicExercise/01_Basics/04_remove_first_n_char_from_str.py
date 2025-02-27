"""
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:

remove_first_n_chars ("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
remove_first_n_chars ("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
Note: n must be less than the length of the string.
"""

def remove_first_n_chars (original_string , n):
    # Removing first 'n' characters from the string
    return original_string [n : ]

original_string  = input("Enter a string : ")
n = int(input("Enter a nber : "))

if n > len(original_string ):
    print("Error : n must be less than the length of the string")
else :
    new_string = remove_first_n_chars (original_string , n)
    print(f"New string after remove {n} chars from orignal string is : {new_string}")

