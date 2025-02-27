import __main__


def generate_full_name(f_name, l_name):
    full_name = f_name + " " + l_name
    return full_name

if __name__ == __main__:
    print("My module is running")
    generate_full_name(f_name="x", l_name="y")
else:
    print("My module is imported")
