"""
Function with Default Parameters
Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.
"""

def get_user_details(fname, age, city="Bidar", pin="585403"):
    print(fname, age, city, pin)

get_user_details("Sourabha", 25)