import numpy as np
def secant(x0,x1): # xk: initial guess
    def f(x):
        return (5-x)*np.exp(x) - 5 # Function of interest
        return f(x0) # Initials for while loop
        return f(x1)
    k = 0
    while abs(f(x1)) >= 10**-8:
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0)) # Secant method formula
        print('x{} = '.format(k+1),x2)
        print('f(x{}) = '.format(k+1),f(x2))
        x0 = x1 # Reassigning
        x1 = x2
        k = k + 1