

'''Add Function'''
def add(x, y):
    return x + y

'''Subtract Function'''
def subtract(x, y):
    return x - y

'''Multiply function'''
def multiply(x, y):
    return x * y

'''Divide function'''
def divide(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y