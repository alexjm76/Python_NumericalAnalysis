import numpy as np

def calc_f(c):
    m = 68.1
    v = 40
    t = 10
    g = 9.81

    return m * g / c * (1 - np.exp(-c / m * t)) - v

r=0
l=12
u=16
while True:
    r = u - ((calc_f(u)*(u-l))/(calc_f(u)-calc_f(l)))
    if calc_f(l)*calc_f(r) < 0:
        u = r
    elif calc_f(l)*calc_f(r) >0:
        l = r
    elif abs(calc_f(r)) < 10**-6:
        print(r)
        break
