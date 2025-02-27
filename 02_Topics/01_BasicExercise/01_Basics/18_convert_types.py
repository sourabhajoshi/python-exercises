print("Convert to int")

int_val, float_val, str_val, comp_val, bool_val = 10, 3.142, "25", 2+3j, True

print("int to int", int(int_val))
print("float to int", int(float_val))
print("str to int", int(str_val))
#print("comp to int", int(comp_val)) # you cannot directly convert a complex number (such as 2+3j) to an integer using int(), because complex numbers have both real and imaginary parts, and integers can only represent real values.
print("bool to int", int(bool_val))


print("-"*50)

print("Convert to float")

int_val, float_val, str_val, comp_val, bool_val = 10, 3.142, "25", 2+3j, True

print("int to int", float(int_val))
print("float to int", float(float_val))
print("str to int", float(str_val))
#print("comp to int", int(comp_val)) # you cannot directly convert a complex number (such as 2+3j) to an integer using int(), because complex numbers have both real and imaginary parts, and integers can only represent real values.
print("bool to int", float(bool_val))


print("-"*50)

print("Convert to bool")

int_val, float_val, str_val, comp_val, bool_val = 10, 3.142, "25", 2+3j, True

print("int to int", bool(int_val))
print("float to int", bool(float_val))
print("str to int", bool(str_val))
#print("comp to int", int(comp_val)) # you cannot directly convert a complex number (such as 2+3j) to an integer using int(), because complex numbers have both real and imaginary parts, and integers can only represent real values.
print("bool to int", bool(bool_val))


print("-"*50)

print("Convert to complex")

int_val, float_val, str_val, comp_val, bool_val = 10, 3.142, "25", 2+3j, True

print("int to int", complex(int_val))
print("float to int", complex(float_val))
print("str to int", complex(str_val))
#print("comp to int", int(comp_val)) # you cannot directly convert a complex number (such as 2+3j) to an integer using int(), because complex numbers have both real and imaginary parts, and integers can only represent real values.
print("bool to int", complex(bool_val))

print("-"*50)