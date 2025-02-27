"""
Write a code which gives grade to students according to theirs scores:

0-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

marks = int(input("Enter your marks : "))
if marks >100 or marks<0:
    print("Please enter your inputs in between 0 to 100")
elif marks<=100 and marks >= 90:
    print("A") 
elif marks<=89 and marks >= 70:
    print("B") 
elif marks<=69 and marks >= 60:
    print("C") 
elif marks<=59 and marks >= 50:
    print("D") 
else:
    print("F")
    