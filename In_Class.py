import numpy as np

def f(x):
    return np.exp(-x) - x

def df(x):
    return -np.exp(-x) - 1

def newton_raphson(x0):
    x = x0
    while abs(f(x)) > 10**-6:
        x -= f(x) / df(x)
    return x
print(f"Newton_Raphson method : {newton_raphson(0)}")

def secant(x0, x1):
    while abs(f(x1)) > 10**-6:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
    return x1

print(f"Secant method : {secant(0,0.01)}")

