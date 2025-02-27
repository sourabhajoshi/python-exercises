# We do not know number of arguments to pass to function such case we use *args
# args used in print_it() is tuple

def print_it(*args):
    for var in args:
        print(var)

print_it(10, "15", "Bidar", 15.22, [1, 2])
# print_it(a=25, v="Joshi", g="Bidar", r=[2, 5], s=(1,)) TypeError: print_it() got an unexpected keyword argument 'a'