"""
Find the length of 'python' and 'dragon' and 
 i. make a falsy comparison statement.
 ii. Use and operator to check if 'on' is found in both 'python' and 'dragon'

 iii. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"""

str1, str2 = "python", "dragon"

print("Length of str1 is {} and Length of str2 is {}".format(len(str1), len(str2)))
print("Are the lengths of str1 and str2 equal?", len(str1) == len(str2))

is_found = "on" in str1 and "on" in str2
print("Use and operator to check if 'on' is found in both 'python' and 'dragon' : ", is_found)

print("-"*50)

sentance = "I hope this course is not full of jargon"
print(f"is 'jargon' fount is sentance? ", "jargon" in sentance)