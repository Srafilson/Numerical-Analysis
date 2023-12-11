from sympy import *
import math
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

fx = sympify(input('Enter function of x >>> '))
h = float(input('central value >>>'))
n = int(input('number of terms to generate >>>'))
eval = float(input('Evaluation point (approximation) >>>'))

print('')
print('f(x) = ' ,fx)
print('')

px = fx.subs(x,h)
fprime = diff(fx)
px = px + fprime.subs(x,h)*(x-h)

print("First derivitive = " , fprime)

for i in range(2,n):
    fprime = diff(fprime)
    px = px + (fprime.subs(x,h)*(x-h)**i)/math.factorial(i)
    if i == 2:
        print('Second derivitve = ' , fprime)
    elif i == 3:
        print("third derivitive = ", fprime)
    else:
        print(i,'th derivitive =', fprime)

print('')
print("Taylor series approximation:" , px)
print('')
print("Approximation at x =", eval)
print(px.subs(x,eval))
print('')
print("actual value")
print(fx.subs(x,eval))
fx_lambda = lambdify(x, fx, 'numpy')
px_lambda = lambdify(x, px, 'numpy')

x_vals = np.linspace(h-10, h+10, 4000)
fx_vals=(fx_lambda(x_vals))
px_vals=(px_lambda(x_vals))

plt.plot(x_vals, fx_vals, label = 'f(x)')
plt.plot(x_vals, px_vals, label = 'taylor approximation')
#plt.ylim(np.min(fx_vals) - 2, np.max(fx_vals) + 2)
plt.legend()
plt.show()
