import numpy as np
import control as ct

delta = 0.1


# xdot = f(x)

#f = np.array([x2,-sin(x1)-delta*x2])
#xbar = np.array([0,0])
x1 = np.pi
x2 = 0

jac = np.array([[0, 1],[-np.cos(x1), -delta]])

 

print(jac)
T, D = np.linalg.eig(jac)

print(T)
print(D)
