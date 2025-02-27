# Python allow a nested functions to access outer scope of enclosing functions

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

clousers_result = add_ten()
print(clousers_result(5))