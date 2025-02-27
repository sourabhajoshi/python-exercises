# Sometime keyword pass to function is not certain, so that time use **kwargs
# as dictionaryt

def print_it(**kwargs):
    for key, value in kwargs.items():
        print("Key : ", key, " value : ", value)

print_it(a=25, v="Joshi", g="Bidar", r=[2, 5], s=(1,))
# print_it(10, 20, 25) #TypeError: print_it() takes 0 positional arguments but 3 were given