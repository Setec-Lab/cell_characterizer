import numpy as np
import control as ct

L = 10e-6
R = 20
C = 10e-6
d = 0.5
vi = 10
il0 = 0
vc0 = 0
Dt  = 0.1


x = np.array([il0, vc0])  #state matrix
A = np.array([[0, -1/L],[1/C, -1/(R*C)]])
u = vi
B = np.array([[d/L],[0]])
eigen,T  = np.linalg.eig(A)
D = np.diag(eigen)

print(np.linalg.matrix_rank(ct.ctrb(A,B))) #is it controllable?


print(A)
Ak = np.exp(A*Dt)
print(Ak)
xk = np.matmul(Ak,x)

print(D)
print(T)

while True:
    xk = xk + 1
