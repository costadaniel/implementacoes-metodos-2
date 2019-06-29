from __future__ import print_function
from math import sqrt, ceil


def ft(t):
    if (t <= 0.5):
        return 4*t
    elif (t <= 1):
        return 4*(1-t)
    else:
        return 0


matricula_franklyn = '397847'
matricula_daniel = '374169'

A, B, C, D, E, F = map(int, list(matricula_franklyn))

m = 1 + (A + B + C + D + E + F) % 4
k = 4
w = sqrt(k/m)
z = 0.05

x0 = (E+F) % 3
xi = 0
t0 = 0
tn = 1.2

h = 0.4
e = 0.0001

y = 0

n = ceil((tn - t0) / h)

for i in range(n):
    xi = x0 + i*h
    k1 = h * ft(xi)
    k2 = h * ft(xi + (h/2))
    k3 = h * ft(xi + (h/2))
    k4 = h * ft(xi + h)
    k = (k1 + 2*k2 + 2*k3 + k4)/6
    y += k
    print(y)

print(y)

print(ft(0.5))
