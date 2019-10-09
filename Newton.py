import numpy as np
def newton(xk): # xk: initial guess
    def f(x):
        return (5-x)*np.exp(x) - 5 # Function of interest
        return f(xk) # Initial for while loop
    def fp(x):
        return (4-x)*np.exp(x) # Derivative of function with respect to x
    k = 0
    while abs(f(xk)) >= 10**-8:
        k = k + 1
        xk = xk - (f(xk)/fp(xk))
        print('xk = ',xk,'for step {}'.format(k))
        print('f(xk) = ',f(xk),'for step {}'.format(k))
    return xk # returns x_star approximation 