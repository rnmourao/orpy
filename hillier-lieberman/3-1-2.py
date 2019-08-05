import numpy as np
from matplotlib import pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

# (a) x1 + 3x2 <= 6
#     x2 <= (6 - x1) / 3
def a(x):
    return (6 - x) / 3


# (b) 4x1 + 3x2 <= 12
#     x2 <= (12 - 4x1) / 3
def b(x):
    return (12 - 4 * x) / 3


# (c) 4x1 + x2 <= 8
#     x2 <= 8 - 4x1
def c(x):
    return 8 - 4 * x


x = Symbol('x')
x1, = solve(a(x) - b(x))
x2, = solve(a(x) - c(x))
x3, = solve(b(x) - c(x))

y1 = a(x1)
y2 = a(x2)
y3 = b(x3)

plt.plot(x1, a(x1), 'go', markersize=10)
plt.plot(x2, a(x2), 'go', markersize=10)
plt.plot(x3, b(x3), 'go', markersize=10)

plt.fill([x1, x2, x3, x1],[y1, y2, y3, y1],'red',alpha=0.5)

xr = np.linspace(0, 10, 100)
y1r = a(xr)
y2r = b(xr)
y3r = c(xr)

plt.plot(xr, y1r, 'k--')
plt.plot(xr, y2r, 'k--')
plt.plot(xr, y3r, 'k--')

# plt.xlim(0.5, 7)
# plt.ylim(2, 8)

plt.show()