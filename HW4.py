import numpy as np
import matplotlib.pyplot as plt

#Taylor series of cos(x) = cos(x0) - sin(x0)/1! (x-x0) - cos(x0)/2!(x-x0)**2 + sin(x0)/3!(x-x0)**3+ ...

#f^{i}(x) = (-1) ** {i/2}xos(x0)/i!, for i =2k ( even )
#f^{i}(x) = (-1)**{(i+1)/2}sin(x0)/i! for i = 2k+1 (odd)

x= np.pi/3
F_true = np.cos(x)
print(F_true) #Q1

#See the effects of increasing the number of the terms of Taylor series expansion.

N_list = [0,1,2,3,4,5,6,7,8,9,10]
h = np.pi/12
err_list = []

for j in N_list:
    x0 = x- h
    F = 0 #Initialize the sum of the Taylor sereis
    for i in range(j+1):
        print("i:", i) #visualize
        if i%2 == 0:
            F += (-1)**(i/2)*np.cos(x0)/np.math.factorial(i)*h**i
        else:
            F += (-1)**((i+1)/2)*np.sin(x0)/np.math.factorial(i)*h**i
    print("Approximated cos(x): ", F, "at", j)
    err = np.abs((F-F_true)/F_true)*100
    err_list.append(err)
    print("Error at ", j, ":", err)


print(err_list)
plt.plot(N_list, err_list, "ko-")
plt.grid()
plt.yscale("log")
plt.ylabel("err in log scale")
plt.xlabel("N-th order Taylor series expansion")
plt.show()

#P2 : Fix N=5 and see the effects of decreasing g(x-x0)

N = 5
h_ref = np.pi/12
h_list = [h_ref,h_ref/2,h_ref/4,h_ref/8,h_ref/16,h_ref/32] #list of h
err_list=[]
for h in h_list:
    x0 = x-h
    print(x0)

    F=0 #initalize the sum of the Taylor series
    for i in range(N+1):
        print("i:", i)  # visualize
        if i % 2 == 0:
            F += (-1) ** (i / 2) * np.cos(x0) / np.math.factorial(i) * h ** i
        else:
            F += (-1) ** ((i + 1) / 2) * np.sin(x0) / np.math.factorial(i) * h ** i
    print("Approximated cos(x): ", F, "at", h)
    err = np.abs((F - F_true) / F_true) * 100
    err_list.append(err)
    print("Error at ", h, ":", err)

print(err_list)
plt.plot(h_list, err_list, "ko-")
plt.plot(h_list, 100*np.power(h_list,6),"mo--", label="Order")
plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.ylabel("err in log scale")
plt.xlabel("h")
plt.legend()
plt.show()
