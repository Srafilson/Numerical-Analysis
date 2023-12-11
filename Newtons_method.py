'''
Newton's method for estimating roots
'''

import math

from sympy import *

import sys






x = symbols('x')
fx = x**3 - 5*x +3
x_0 = 3
nmax = 10
epsilon = 0.0005



x_new = float(x_0)
fp = diff(fx)
print("")
print("Using Newton's method to approximate the root of the function f(x) =", fx)
print('')
print('n = ', 0, 'x_n = ', x_new, 'f(x) = ', fx.subs(x, x_new))
for i in range(1,nmax+1):
    fpx = fp.subs(x,x_new)
    if abs(fpx) < epsilon:
        print("small derivitive: f'(x) = ", fp)
        break
    d = fx.subs(x, x_new)/fpx
    x_new = x_new - d
    print('n = ', i, 'x_n = ', x_new, 'f(x) = ', fx.subs(x, x_new))
    if abs(d) < epsilon:
        print("Convergence: f(x)/f'(x) < epsilon")
        break
