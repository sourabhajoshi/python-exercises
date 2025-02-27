"""
For instance if you want to generate a list of numbers
"""

num = int(input("Enter a number : "))

num_list = [ i for i in range(num+1)]

square_list = [i*i for i in range(num+1)]

tupel_list = [(i, i*i) for i in range(num+1)]

print("Number List : ", num_list)
print("Square List : ", square_list)
print("Tuple list : ", tupel_list)