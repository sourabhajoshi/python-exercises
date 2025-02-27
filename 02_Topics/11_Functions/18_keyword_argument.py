# in keyword arg, no need to maintain a positional order while passing the arguments
# based on the keyword py interpreter set the value correctly and perform task


def sum_of_num(a, b, c, d):
    res = a+b+c+d
    print(a, b, c, d)
    print("Sum of nums : ", res)

sum_of_num(a=10, c=15, d=25, b=5)