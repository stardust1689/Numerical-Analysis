 import numpy as np 
#Allows for built-in math functions (sin(), exp(), etc.)
def bisect(a,b):
    def f(x):
        return (5-x)*np.exp(x) - 5 
        # Function of interest
    if f(a)*f(b) < 0:
        k = 0
        while k <= 10:
        # k <= "number of iterations"
            k = k + 1
            x_k = (a+b)/2
            if f(a)*f(x_k) < 0:
                b = x_k
            elif f(b)*f(x_k) < 0:
                a = x_k
        return x_k
        # Returns x_star approximation
    else:
        return 'No solution enclosed'