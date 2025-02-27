# Function can be assigned to any variable and we can call fun using that variable

def sum(a, b):
    print("Sum is : ", a+b)

f = sum
f(2, 5)

g = sum
g(25, 50)

# Function can be passed as argument and function can be return from fun

def sum_two(a, b, f):
    print(a+b)
    f()

def func():
    print("Hello Func")

f = func

sum_two(10, 15, f)