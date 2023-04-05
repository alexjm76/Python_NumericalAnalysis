import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x) - x

def df(x):
    return -np.exp(-x) - 1

def newton_raphson(x0):
    x = x0
    xr_list = []
    Iteration_list = []
    while abs(f(x)) >= 10**-6:
        x -= f(x) / df(x)
        xr_list.append(x)
        Iteration_list.append(abs(f(x)))

    return xr_list, Iteration_list

def secant(x0, x1):
    xr_list = []
    Iteration_list = []
    while abs(f(x1)) >= 10**-6:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        xr_list.append(x1)
        Iteration_list.append(abs(f(x1)))

    return xr_list, Iteration_list

# Call the functions
xr_newton, Iter_newton = newton_raphson(0)
xr_secant, Iter_secant = secant(0, 0.01)

# Plot the results
plt.plot(range(len(Iter_newton)), Iter_newton, label="Newton-Raphson")
plt.plot(range(len(Iter_secant)), Iter_secant, label="Secant")
# plt.xlim([1.0, 4.0])
plt.grid()
plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("|f(xr)|")
plt.legend()
plt.show()


