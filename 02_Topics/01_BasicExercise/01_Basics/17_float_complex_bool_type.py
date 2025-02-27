import sys
print("Use of float")

a, b = 3.142, 10

print("Add of a and b : ", a + b)
print("Sub of a and b : ",(a - b), "round upto 2 decimal values : ", round((a - b), 2))
print("Mul of a and b : ", a * b)
print("Div of a and b : ", a / b) # yield in factorial form
print("Mod of a and b : ", a % b) # yield quotient
print("Floor Div of a and b : ", a // b) # yield in int form
print("Expo of a and b : ", a ** b)
print("type of b :", type(b))
print("Memory address of b :", id(b))
print("Size of b :", sys.getsizeof(b))
print("is \"a\" intsnce of float", isinstance(a, float))

print("-" *50)

print("use of Complex")
a = 2 + 3j
print("Real part : ", a.real)
print("Imaginary part : ", a.imag)
print("Orignal complex no : ", a, "Mul with 2 : ", a*2)

print("-" *50)

print("use of bool")

a = True
b = False

print("value of a :", a)
print("value of b :", b)
print("type of b :", type(b))
print("Memory address of b :", id(b))
print("Size of b :", sys.getsizeof(b))
print("is \"b\" intsnce of bool", isinstance(b, bool))