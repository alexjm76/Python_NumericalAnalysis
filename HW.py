import numpy as np
import matplotlib.pyplot as plt

def calc_f(c):
    m = 68.1
    v = 40
    t = 10
    g = 9.81

    return m * g / c * (1 - np.exp(-c / m * t)) - v

r=0
l=12
u=16



def Bisection(l, u, tolerance=1e-6, max_iterations=1000):
    num = 0
    num_r = []
    iteration = []
    while num < max_iterations:
        r = (l + u) / 2
        if abs(calc_f(r)) < tolerance:
            break
        elif calc_f(l) * calc_f(r) < 0:
            u = r
            num += 1
            iteration.append(num)
            num_r.append(abs(calc_f(r)))
        else:
            l = r
            num += 1
            iteration.append(num)
            num_r.append(abs(calc_f(r)))
    return iteration, num_r


def False_position(l, u, tolerance=1e-6, max_iterations=1000):
    num = 0
    num_r = []
    iteration = []
    while num < max_iterations:
        r = u - ((calc_f(u) * (u - l)) / (calc_f(u) - calc_f(l)))
        if abs(calc_f(r)) < tolerance:
            break
        elif calc_f(l) * calc_f(r) < 0:
            u = r
            num += 1
            iteration.append(num)
            num_r.append(abs(calc_f(r)))
        else:
            l = r
            num += 1
            iteration.append(num)
            num_r.append(abs(calc_f(r)))
    return iteration, num_r
print(Bisection(l,u))
print(False_position(l,u))

Bi_it, Bi_num =  Bisection(l,u)
F_it, f_num = False_position(l,u)


plt.plot(Bi_it,Bi_num,F_it,f_num,marker="o")
plt.grid()
plt.yscale("log")
plt.ylabel("f(x_{r})")
plt.xlabel("Iteration")
plt.title("Iteration vs f(x_{r})")
plt.show()
